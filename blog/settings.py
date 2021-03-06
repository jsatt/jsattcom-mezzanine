
from __future__ import absolute_import, unicode_literals
import os

from django import VERSION as DJANGO_VERSION
from django.utils.translation import ugettext_lazy as _
from environ import Env

env = Env()


######################
# MEZZANINE SETTINGS #
######################

# The following settings are already defined with default values in
# the ``defaults.py`` module within each of Mezzanine's apps, but are
# common enough to be put here, commented out, for conveniently
# overriding. Please consult the settings documentation for a full list
# of settings Mezzanine implements:
# http://mezzanine.jupo.org/docs/configuration.html#default-settings

# Controls the ordering and grouping of the admin menu.
#
# ADMIN_MENU_ORDER = (
#     ("Content", ("pages.Page", "blog.BlogPost",
#        "generic.ThreadedComment", (_("Media Library"), "media-library"),)),
#     ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting")),
#     ("Users", ("auth.User", "auth.Group",)),
# )

# A three item sequence, each containing a sequence of template tags
# used to render the admin dashboard.
#
# DASHBOARD_TAGS = (
#     ("blog_tags.quick_blog", "mezzanine_tags.app_list"),
#     ("comment_tags.recent_comments",),
#     ("mezzanine_tags.recent_actions",),
# )

# A sequence of templates used by the ``page_menu`` template tag. Each
# item in the sequence is a three item sequence, containing a unique ID
# for the template, a label for the template, and the template path.
# These templates are then available for selection when editing which
# menus a page should appear in. Note that if a menu template is used
# that doesn't appear in this setting, all pages will appear in it.

PAGE_MENU_TEMPLATES = (
    (1, _("Top navigation bar"), "pages/menus/dropdown.html"),
#     (2, _("Left-hand tree"), "pages/menus/tree.html"),
    (3, _("Footer"), "pages/menus/footer.html"),
)

# A sequence of fields that will be injected into Mezzanine's (or any
# library's) models. Each item in the sequence is a four item sequence.
# The first two items are the dotted path to the model and its field
# name to be added, and the dotted path to the field class to use for
# the field. The third and fourth items are a sequence of positional
# args and a dictionary of keyword args, to use when creating the
# field instance. When specifying the field class, the path
# ``django.models.db.`` can be omitted for regular Django model fields.
#
# EXTRA_MODEL_FIELDS = (
#     (
#         # Dotted path to field.
#         "mezzanine.blog.models.BlogPost.image",
#         # Dotted path to field class.
#         "somelib.fields.ImageField",
#         # Positional args for field class.
#         (_("Image"),),
#         # Keyword args for field class.
#         {"blank": True, "upload_to": "blog"},
#     ),
#     # Example of adding a field to *all* of Mezzanine's content types:
#     (
#         "mezzanine.pages.models.Page.another_field",
#         "IntegerField", # 'django.db.models.' is implied if path is omitted.
#         (_("Another name"),),
#         {"blank": True, "default": 1},
#     ),
# )

# Setting to turn on featured images for blog posts. Defaults to False.
#
# BLOG_USE_FEATURED_IMAGE = True

# If True, the django-modeltranslation will be added to the
# INSTALLED_APPS setting.
USE_MODELTRANSLATION = False


########################
# MAIN DJANGO SETTINGS #
########################

SECRET_KEY = env.str('SECRET_KEY', default='')
NEVERCACHE_KEY = env.str('NEVERCACHE_KEY', default='')

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = env.str('TIME_ZONE', default='UTC')

# If you set this to True, Django will use timezone-aware datetimes.
USE_TZ = env.bool('USE_TZ', default=True)

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en"

# Supported languages
LANGUAGES = (
    ('en', _('English')),
)

# A boolean that turns on/off debug mode. When set to ``True``, stack traces
# are displayed for error pages. Should always be set to ``False`` in
# production. Best set to ``True`` in local_settings.py
DEBUG = env.bool('DEBUG', default=False)

# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

AUTHENTICATION_BACKENDS = ("mezzanine.core.auth_backends.MezzanineBackend",)

# The numeric mode to set newly-uploaded files to. The value should be
# a mode you'd pass directly to os.chmod.
FILE_UPLOAD_PERMISSIONS = 0o644


#############
# DATABASES #
#############

DATABASES = {
    "default": env.db('DATABASE_URL', default='sqlite://mezzanine.db')
}


#########
# PATHS #
#########

# Full filesystem path to the project.
PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_APP = os.path.basename(PROJECT_APP_PATH)
PROJECT_ROOT = BASE_DIR = os.path.dirname(PROJECT_APP_PATH)

# Every cache key will get prefixed with this value - here we set it to
# the name of the directory the project is in to try and use something
# project specific.
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_APP

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = env.str('STATIC_URL', default="/static/")

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = env.str('STATIC_ROOT', default=os.path.join(PROJECT_ROOT, STATIC_URL.strip("/")))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = env.str('MEDIA_URL', default=STATIC_URL + "media/")

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = env.str('MEDIA_ROOT',
                     default=os.path.join(PROJECT_ROOT, *MEDIA_URL.strip("/").split("/")))

# Package/module name to import the root urlpatterns from for the project.
ROOT_URLCONF = "%s.urls" % PROJECT_APP

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_ROOT, "templates")
        ],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.static",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.tz",
                "mezzanine.conf.context_processors.settings",
                "mezzanine.pages.context_processors.page",
            ],
            "builtins": [
                "mezzanine.template.loader_tags",
            ],
            "loaders": [
                "mezzanine.template.loaders.host_themes.Loader",
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ]
        },
    },
]

if DJANGO_VERSION < (1, 9):
    del TEMPLATES[0]["OPTIONS"]["builtins"]


################
# APPLICATIONS #
################

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.pages",
    "mezzanine.blog",
    "mezzanine.forms",
    "mezzanine.galleries",
    "mezzanine.twitter",
    # "mezzanine.accounts",

    'customizations',
    'ckeditor',
)

# List of middleware classes to use. Order is important; in the request phase,
# these middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE = (
    "mezzanine.core.middleware.UpdateCacheMiddleware",

    'django.contrib.sessions.middleware.SessionMiddleware',
    # Uncomment if using internationalisation or localisation
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "mezzanine.core.request.CurrentRequestMiddleware",
    "mezzanine.core.middleware.RedirectFallbackMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    "mezzanine.core.middleware.SitePermissionMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "mezzanine.core.middleware.FetchFromCacheMiddleware",
)

if DJANGO_VERSION < (1, 10):
    MIDDLEWARE_CLASSES = MIDDLEWARE
    del MIDDLEWARE


# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"

#########################
# OPTIONAL APPLICATIONS #
#########################

# These will be added to ``INSTALLED_APPS``, only if available.
OPTIONAL_APPS = (
    "debug_toolbar",
    "django_extensions",
    "compressor",
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)

DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False}
#TINYMCE_SETUP_JS = 'js/tinymce_setup.js'
RICHTEXT_WIDGET_CLASS = 'customizations.widgets.CustomCKEditorWidget'
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_SOURCE = STATIC_URL + 'js/ckeditor/ckeditor.js'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
        'skin': 'moonocolor',
        'toolbarGroups': [
            { 'name': 'styles' },
            { 'name': 'basicstyles', 'groups': [ 'basicstyles', 'cleanup' ] },
            { 'name': 'paragraph',   'groups': [ 'list', 'indent', 'blocks', 'align', 'bidi' ] },
            { 'name': 'insert' },
            '/',
            { 'name': 'clipboard',   'groups': [ 'clipboard', 'undo' ] },
            { 'name': 'editing',     'groups': [ 'find', 'selection', 'spellchecker' ] },
            { 'name': 'links' },
            { 'name': 'forms' },
            { 'name': 'tools' },
            { 'name': 'documet',     'groups': [ 'mode', 'document', 'doctools' ] },
            { 'name': 'others' },
            { 'name': 'colors' },
            { 'name': 'about' }
        ],
        'extraAllowedContent': {
            'pre code nav ul ol li abbr': {
                'classes': '*'
            },
            'h1 h2 h3 h4 h5 h6':{
                'attributes': 'id'
            },
            'style script': {},
            'input button checkbox select radio': {},
            '*': {
                'attributes': '*',
            },
        },
        'contentsCss': (
            STATIC_URL + 'css/bootstrap.min.css',
            STATIC_URL + 'css/main.css',
        ),
    }
}

STATICFILES_STORAGE = env.str(
    'STATICFILES_STORAGE',
    default='django.contrib.staticfiles.storage.StaticFilesStorage')
STATICFILES_LOCATION = env.str('STATICFILES_LOCATION', default='')
DEFAULT_FILE_STORAGE = env.str(
    'DEFAULT_FILE_STORAGE',
    default='django.core.files.storage.FileSystemStorage')
MEDIA_LOCATION = env.str('MEDIA_LOCATION', default='')


aws_key = env.str('AWS_ACCESS_KEY_ID', default=None)
if aws_key is not None:
    AWS_ACCESS_KEY_ID = aws_key
aws_secret = env.str('AWS_SECRET_ACCESS_KEY', default=None)
if aws_secret is not None:
    AWS_SECRET_ACCESS_KEY = aws_secret
aws_bucket = env.str('AWS_STORAGE_BUCKET_NAME', default=None)
if aws_bucket is not None:
    AWS_STORAGE_BUCKET_NAME = aws_bucket
aws_qs_auth = env.bool('AWS_QUERYSTRING_AUTH', default=None)
if aws_qs_auth is not None:
    AWS_QUERYSTRING_AUTH = aws_qs_auth
aws_s3_encrypt = env.bool('AWS_S3_ENCRYPTION', default=None)
if aws_s3_encrypt is not None:
    AWS_S3_ENCRYPTION = aws_s3_encrypt
aws_acl = env.bool('AWS_DEFAULT_ACL', default=None)
if aws_acl is not None:
    AWS_DEFAULT_ACL = aws_acl
aws_file_overwrite = env.bool('AWS_S3_FILE_OVERWRITE', default=None)
if aws_file_overwrite is not None:
    AWS_S3_FILE_OVERWRITE = aws_file_overwrite
aws_location = env.str('AWS_LOCATION', default=None)
if aws_location is not None:
    AWS_LOCATION = aws_location
aws_s3_domain = env.str('AWS_S3_CUSTOM_DOMAIN', default=None)
if aws_s3_domain is not None:
    AWS_S3_CUSTOM_DOMAIN = aws_s3_domain

####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())
