from django.contrib import admin
from .models import addinfo, Notices, queries
# Register your models here.
admin.site.register(addinfo)
admin.site.register(Notices)
admin.site.register(queries)
