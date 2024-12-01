from django.contrib import admin
from .models import RFIDUser, AccessLog

admin.site.register(RFIDUser)
admin.site.register(AccessLog)

