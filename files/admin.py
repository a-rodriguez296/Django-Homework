from django.contrib import admin
from models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'created_on', 'modified_on',)


admin.site.register(File, FileAdmin)