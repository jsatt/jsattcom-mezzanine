from django.db import models
from mezzanine.pages.models import Page

class StaticPage(Page):
    content = models.TextField("Content")
