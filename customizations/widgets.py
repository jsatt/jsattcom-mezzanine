from ckeditor.widgets import CKEditorWidget
from django.conf import settings


class CustomCKEditorWidget(CKEditorWidget):
    class Media:
        extend = False
        js = (
            getattr(settings, 'CKEDITOR_SOURCE',
                    settings.STATIC_URL + 'ckeditor/ckeditor/ckeditor.js'),
        )
