from django.contrib import admin
from groups.models import Group, StudySession 


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class StudySessionAdmin(admin.ModelAdmin):
    list_display = ('description', 'date')


admin.site.register(Group, GroupAdmin)
admin.site.register(StudySession, StudySessionAdmin)
