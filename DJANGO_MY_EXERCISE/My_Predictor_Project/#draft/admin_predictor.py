from django.contrib import admin
from . import models

# Register your models here.

class DisciplineAdmin(admin.ModelAdmin):
    pass

class TournamentAdmin(admin.ModelAdmin):
    pass

class GroupAdmin(admin.ModelAdmin):
    pass

class GroupStartPositionAdmin(admin.ModelAdmin):
    pass

class TeamAdmin(admin.ModelAdmin):
    pass

class TournamentMemberAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Discipline)
admin.site.register(models.Tournament)
admin.site.register(models.Group)
admin.site.register(models.GroupStartPosition)
admin.site.register(models.Team)
admin.site.register(models.TournamentMember)
