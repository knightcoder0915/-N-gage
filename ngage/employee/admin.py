from django.contrib import admin

# Register your models here.

from embed_video.admin import AdminVideoMixin
from .models import tutorial

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(tutorial, MyModelAdmin)
