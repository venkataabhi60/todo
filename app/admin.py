from django.contrib import admin

from app.models import Task
class TaskAdmin(admin.ModelAdmin):
    list_display=('task','is_completed','updated_at','created_at')
    search_fields=('task',)
admin.site.register(Task,TaskAdmin)