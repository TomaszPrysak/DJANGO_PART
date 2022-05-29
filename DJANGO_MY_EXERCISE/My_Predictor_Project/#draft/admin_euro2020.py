from django.contrib import admin
from . import models

# Register your models here.

class GroupAdmin(admin.ModelAdmin):
    pass

class TeamAdmin(admin.ModelAdmin):
    pass

class GroupMemberAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Group)
admin.site.register(models.Team)
admin.site.register(models.GroupMember)
