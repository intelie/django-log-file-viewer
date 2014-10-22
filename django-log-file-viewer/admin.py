
from django.contrib import admin
from models import LogFile
import templatetags.paginator_tags # so tags get registered

class LogFileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

admin.site.register(LogFile, LogFileAdmin)
