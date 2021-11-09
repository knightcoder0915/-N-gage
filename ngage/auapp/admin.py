
from django.contrib import admin

from .models import DeleteModel
admin.site.register(DeleteModel)

from .models import EventsModel
admin.site.register(EventsModel)
