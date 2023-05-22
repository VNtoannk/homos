from django.contrib import admin
from .models import Site, IP_public_test

# Register your models here.

admin.site.register(Site)
admin.site.register(IP_public_test)
