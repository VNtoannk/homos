from django.contrib import admin
from . models import CountryData, TaskDue

# Register your models here.
admin.site.register(CountryData)
admin.site.register(TaskDue)