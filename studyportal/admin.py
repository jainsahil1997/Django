from django.contrib import admin

# Register your models here.
from .models import Department, Subject, Material
admin.site.register(Department)
admin.site.register(Subject)
admin.site.register(Material)
