from django.contrib import admin
from .models import Credentials


admin.site.name = "E-Vote"
admin.site.site_header = "E-Vote Administration"
admin.site.site_title = "E-Vote Admin Portal"
admin.site.index_title = "Welcome to E-Vote Admin Portal"

# Register your models here.

admin.site.register(Credentials)


