from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import Myadmin

# Register your models here.
admin.site.register(Myadmin)

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'expire_date', 'get_decoded']

    def get_decoded(self, obj):
        return obj.get_decoded()
    get_decoded.short_description = "Decoded Data"