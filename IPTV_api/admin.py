from django.contrib import admin
from . import models
admin.site.register(models.Plan),
admin.site.register(models.Subscription),
admin.site.register(models.Payment),
admin.site.register(models.KeywordsDescriptionHome),
