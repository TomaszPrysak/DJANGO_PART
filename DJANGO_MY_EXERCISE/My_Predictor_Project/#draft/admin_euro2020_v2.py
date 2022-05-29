from django.contrib import admin
from . import models
from django import forms
from django.utils import timezone
from django.utils.timezone import localtime
from django.db.models import Q, F, Func, Value, CharField
from django.core.exceptions import ValidationError
import pytz
from datetime import datetime
from django.db.models.functions import (
        ExtractDay, ExtractHour, ExtractMinute, ExtractMonth,
        ExtractQuarter, ExtractSecond, ExtractWeek, ExtractIsoWeekDay,
        ExtractWeekDay, ExtractIsoYear, ExtractYear)

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
                    'date']

class GroupMatchScoreAdmin(admin.ModelAdmin):
    list_display = ['group_match', 'host_goals', 'guest_goals']

class GroupMatchPredictForm(forms.ModelForm):
    class Meta:
        model = models.GroupMatchPredict
        fields = '__all__'

    def clean(self):
        datePredict = timezone.now()
        host_team = str(self.cleaned_data['group_match']).split(' - ')[0].split('/')[-1]
        id_host_team = models.Team.objects.filter(name=host_team).values_list('id', flat=True)
        guest_team = str(self.cleaned_data['group_match']).split(' - ')[1].split('/')[-1]
        id_guest_team = models.Team.objects.filter(name=guest_team).values_list('id', flat=True)

        # dateMatch = models.GroupMatch.objects.filter(
        #                                             host__team__name=host_team, guest__team__name = guest_team
        #                                             ).values_list(
        #                                                          'date', flat=True
        #                                                          ).extra(
        #                                                                 select={'date':"DATE(date, 'YYYY-MM-DD hh:mi')"}
        #                                                                 )

        # dateMatch = models.GroupMatch.objects.filter(
        #                                             host__team__name=host_team, guest__team__name = guest_team
        #                                             ).values_list(
        #                                                          'date', flat=True
        #                                                          ).extra(
        #                                                                 select={'date':"to_char(euro2020_GroupMatch.date, 'YYYY-MM-DD hh:mi AM')"}
        #                                                                 )

        # dateMatch = models.GroupMatch.objects.filter(
        #                                             host__team__name=host_team, guest__team__name = guest_team
        #                                             ).values_list(
        #                                                          'date', flat=True
        #                                                          ).extra(
        #                                                                 select={'date':"DATE_FORMAT('YYYY-MM-DD hh:mi AM')"}
                                                                        # )

        dateMatchTest = models.GroupMatch.objects.filter(host__team__name=host_team, guest__team__name = guest_team).values_list('date', flat=True)

        print(dateMatchTest[0])

        dateMatch = models.GroupMatch.objects.filter(
                                                        host__team__name=host_team, guest__team__name = guest_team
                                                    ).values_list(
                                                                    'date', flat=True
                                                                  ).annotate(
                                                                                year=ExtractYear('date'),
                                                                                month=ExtractMonth('date'),
                                                                                day=ExtractDay('date'),
                                                                                weekday=ExtractWeekDay('date'),
                                                                                hour=ExtractHour('date'),
                                                                                minute=ExtractMinute('date'),
                                                                                second=ExtractSecond('date'),
                                                                            ).values('year', 'month', 'day', 'hour', 'minute', 'second')

        # print(host_team, guest_team)
        print(datePredict)
        # print(dateMatch[0])

        if datePredict <= dateMatchTest[0]:
            print("możesz obstawiać")
        else:
            print('nie możesz obstawiać')
        # if subcategory is None:
        #     return self.cleaned_data
        # else:
        #     try:
        #         category = self.cleaned_data['category']
        #         subcategory_category = Subcategory.objects.get(pk=subcategory.pk).main_category
        #         if subcategory_category == category:
        #             return self.cleaned_data
        #         else:
        #             raise ValidationError()
        #     except:
        #         msg = "Podkategoria '{0}' nie należy do kategorii '{1}'. Sprawdź w 'Subcategorys' przynależność podkategorii do głównej kategorii.".format("test", "test2")
        #         raise ValidationError(msg)

class GroupMatchPredictAdmin(admin.ModelAdmin):
    form = GroupMatchPredictForm

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
