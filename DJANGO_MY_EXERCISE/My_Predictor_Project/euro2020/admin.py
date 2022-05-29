from django.contrib import admin
from . import models
from django import forms
from django.utils import timezone
from django.utils.timezone import localtime
from django.db.models import Q, F, Func, Value, CharField
from django.core.exceptions import ValidationError
import pytz
from datetime import datetime

# Register your models here.

class TournamentMemberAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'points']

class GroupAdmin(admin.ModelAdmin):
    pass

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'played',
                    'won',
                    'drawn',
                    'lost',
                    'goal_for',
                    'goal_against',
                    'goal_difference',
                    'points']

class StartPositionAdmin(admin.ModelAdmin):
    pass

class GroupMemberAdmin(admin.ModelAdmin):
    list_filter = ['group']
    list_display = ['group',
                    'team',
                    'played',
                    'won',
                    'drawn',
                    'lost',
                    'goal_for',
                    'goal_against',
                    'goal_difference',
                    'points',
                    'position_at_start']

class GroupMatchAdmin(admin.ModelAdmin):
    list_filter = ['group']
    list_display = ['group',
                    'host',
                    'guest',
                    'date',]

class GroupMatchScoreAdmin(admin.ModelAdmin):
    list_display = ['group_match', 'host_goals', 'guest_goals']

class GroupMatchPredictForm(forms.ModelForm):
    class Meta:
        model = models.GroupMatchPredict
        fields = '__all__'

    def clean(self):
        datePredictLTZ = timezone.localtime()
        host_team = str(self.cleaned_data['group_match']).split(' - ')[0].split('/')[-1]
        guest_team = str(self.cleaned_data['group_match']).split(' - ')[1].split('/')[-1]
        dateMatchLTZ = timezone.localtime(models.GroupMatch.objects.filter(host__team__name=host_team, guest__team__name = guest_team).values_list('date', flat=True)[0])

        if datePredictLTZ <= dateMatchLTZ:
            return self.cleaned_data
        else:
            try:
                raise ValidationError()
            except:
                msg = "Nie zdążyłeś. Nie można obstawiać meczu po jego rozpoczęciu się. Data i godzina Twojego obstawiania to: '{0}'.\nData i godzina rozpoczęcia obstawianego meczu to: '{1}'.".format(datePredictLTZ.strftime('%Y-%m-%d %H:%M'), dateMatchLTZ.strftime('%Y-%m-%d %H:%M'))
                raise ValidationError(msg)

class GroupMatchPredictAdmin(admin.ModelAdmin):
    form = GroupMatchPredictForm

    def save_model(self, request, obj, form, change):
        if obj.user_predict == request.user or request.user.is_superuser:
            try:
                obj.date = timezone.now()
                super().save_model(request, obj, form, change)
            except:
                pass

    list_display = ['user_predict',
                    'group_match',
                    'date',
                    'host_goals',
                    'guest_goals']

admin.site.register(models.TournamentMember,TournamentMemberAdmin)
admin.site.register(models.Group)
admin.site.register(models.Team, TeamAdmin)
admin.site.register(models.StartPosition)
admin.site.register(models.GroupMember, GroupMemberAdmin)
admin.site.register(models.GroupMatch, GroupMatchAdmin)
admin.site.register(models.GroupMatchScore, GroupMatchScoreAdmin)
admin.site.register(models.GroupMatchPredict, GroupMatchPredictAdmin)
