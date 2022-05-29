from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import F
from . import models
from django.utils import timezone
from django.contrib.auth.models import User

@receiver(post_save, sender=models.GroupMatch)
def post_save_create_match_score(sender, instance, created, **kwargs):
    # print(sender)
    # print(instance)
    # print(created)
    if created:
        models.GroupMatchScore.objects.create(group_match=instance)

@receiver(post_save, sender=models.GroupMatchScore)
def post_save_update_team_statistic(sender, instance, created, **kwargs):
    if not created:
        # print(sender)
        # print(instance)
        # print(created)
        # print(models.GroupMember.objects.get(team__name=hostTeam).code_position_at_start)

        hostTeam = instance.group_match.host.team.name
        hostTeamGoals = instance.host_goals

        guestTeam = instance.group_match.guest.team.name
        guestTeamGoeals = instance.guest_goals

        ###
        # Uzupełnienie statystyk drużyn w fazie grupowej
        models.GroupMember.objects.filter(team__name=hostTeam).update(played = F('played') + 1)
        models.GroupMember.objects.filter(team__name=guestTeam).update(played = F('played') + 1)

        models.GroupMember.objects.filter(team__name=hostTeam).update(goal_for = F('goal_for') + hostTeamGoals, goal_against = F('goal_against') + guestTeamGoeals)
        models.GroupMember.objects.filter(team__name=hostTeam).update(goal_difference = models.GroupMember.objects.get(team__name=hostTeam).goal_for - models.GroupMember.objects.get(team__name=hostTeam).goal_against)
        models.GroupMember.objects.filter(team__name=guestTeam).update(goal_for = F('goal_for') + guestTeamGoeals, goal_against = F('goal_against') + hostTeamGoals)
        models.GroupMember.objects.filter(team__name=guestTeam).update(goal_difference = models.GroupMember.objects.get(team__name=guestTeam).goal_for - models.GroupMember.objects.get(team__name=guestTeam).goal_against)

        if hostTeamGoals > guestTeamGoeals:
            models.GroupMember.objects.filter(team__name=hostTeam).update(points = F('points') + 3)
            models.GroupMember.objects.filter(team__name=hostTeam).update(won = F('won') + 1)
            models.GroupMember.objects.filter(team__name=guestTeam).update(lost = F('lost') + 1)
        elif hostTeamGoals == guestTeamGoeals:
            models.GroupMember.objects.filter(team__name=hostTeam).update(points = F('points') + 1)
            models.GroupMember.objects.filter(team__name=guestTeam).update(points = F('points') + 1)
            models.GroupMember.objects.filter(team__name=hostTeam).update(drawn = F('drawn') + 1)
            models.GroupMember.objects.filter(team__name=guestTeam).update(drawn = F('drawn') + 1)
        else:
            models.GroupMember.objects.filter(team__name=guestTeam).update(points = F('points') + 3)
            models.GroupMember.objects.filter(team__name=guestTeam).update(won = F('won') + 1)
            models.GroupMember.objects.filter(team__name=hostTeam).update(lost = F('lost') + 1)

        ###
        # Uzupełnienie statystyk drużyn w całym turnieju
        models.Team.objects.filter(name=hostTeam).update(played = F('played') + 1)
        models.Team.objects.filter(name=guestTeam).update(played = F('played') + 1)

        models.Team.objects.filter(name=hostTeam).update(goal_for = F('goal_for') + hostTeamGoals, goal_against = F('goal_against') + guestTeamGoeals)
        models.Team.objects.filter(name=hostTeam).update(goal_difference = models.Team.objects.get(name=hostTeam).goal_for - models.Team.objects.get(name=hostTeam).goal_against)
        models.Team.objects.filter(name=guestTeam).update(goal_for = F('goal_for') + guestTeamGoeals, goal_against = F('goal_against') + hostTeamGoals)
        models.Team.objects.filter(name=guestTeam).update(goal_difference = models.Team.objects.get(name=guestTeam).goal_for - models.Team.objects.get(name=guestTeam).goal_against)

        if hostTeamGoals > guestTeamGoeals:
            models.Team.objects.filter(name=hostTeam).update(points = F('points') + 3)
            models.Team.objects.filter(name=hostTeam).update(won = F('won') + 1)
            models.Team.objects.filter(name=guestTeam).update(lost = F('lost') + 1)
        elif hostTeamGoals == guestTeamGoeals:
            models.Team.objects.filter(name=hostTeam).update(points = F('points') + 1)
            models.Team.objects.filter(name=guestTeam).update(points = F('points') + 1)
            models.Team.objects.filter(name=hostTeam).update(drawn = F('drawn') + 1)
            models.Team.objects.filter(name=guestTeam).update(drawn = F('drawn') + 1)
        else:
            models.Team.objects.filter(name=guestTeam).update(points = F('points') + 3)
            models.Team.objects.filter(name=guestTeam).update(won = F('won') + 1)
            models.Team.objects.filter(name=hostTeam).update(lost = F('lost') + 1)

        ###
        # Uzupełnienie statystyk użytkowników
        listMatchPredict = models.GroupMatchPredict.objects.filter(group_match__host__team__name=hostTeam, group_match__guest__team__name = guestTeam).values_list('user_predict', 'host_goals', 'guest_goals')

        for match in listMatchPredict:
            userName = models.User.objects.filter(pk=match[0])[0]
            userPredictHostGoals = match[1]
            userPredictGuestGoals = match[2]
            # print(userName, userPredictHostGoals, userPredictGuestGoals)

            if userPredictHostGoals == hostTeamGoals and userPredictGuestGoals == guestTeamGoeals:
                models.TournamentMember.objects.filter(user=userName).update(points = F('points') + 3)
            elif userPredictHostGoals > userPredictGuestGoals and hostTeamGoals > guestTeamGoeals:
                models.TournamentMember.objects.filter(user=userName).update(points = F('points') + 1)
            elif userPredictHostGoals < userPredictGuestGoals and hostTeamGoals < guestTeamGoeals:
                models.TournamentMember.objects.filter(user=userName).update(points = F('points') + 1)
            elif userPredictHostGoals == userPredictGuestGoals and hostTeamGoals == guestTeamGoeals:
                models.TournamentMember.objects.filter(user=userName).update(points = F('points') + 1)

# @receiver(post_save,
# def post_save_user_prediction_score_match(sender, instance, created, **kwargs):
#     print(sender)
#     print(instance)
#     print(created)
