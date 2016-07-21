from django.contrib import admin
from mezzanine.pages.admin import PageAdmin

from .models import StaticPage

admin.site.register(StaticPage, PageAdmin)
