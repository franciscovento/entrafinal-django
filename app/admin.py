from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Author)
admin.site.register(models.Category)
admin.site.register(models.Rack)
admin.site.register(models.Book)
