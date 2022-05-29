from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class TournamentMember(models.Model):
    user = models.OneToOneField(User, related_name='user_tournament', on_delete=models.CASCADE)
    points = models.PositiveSmallIntegerField(default=0, help_text='Enter the number of points get by user')

    class Meta:
        verbose_name_plural = "Users members"

    def __str__(self):
        return self.user.username

class Group(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='Enter group name')
    slug = models.SlugField(allow_unicode=True, max_length=100, unique=True, editable=False, default='')

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='Enter team name')
    slug = models.SlugField(allow_unicode=True, max_length=100, unique=True, editable=False, default='')

    played = models.PositiveSmallIntegerField(default=0, help_text='Enter the number of played match by team')
    won = models.PositiveSmallIntegerField(default=0, help_text='Enter the number of won match by team')
    drawn = models.PositiveSmallIntegerField(default=0, help_text='Enter the number of drawn match by team')
    lost = models.PositiveSmallIntegerField(default=0, help_text='Enter the number of lost match by team')
    goal_for = models.PositiveSmallIntegerField(default=0, help_text='Enter the number of goals scored by team')
    goal_against = models.PositiveSmallIntegerField(default=0, help_text='Enter the number of goals lost by team')
    goal_difference = models.SmallIntegerField(default=0, help_text='Enter the difference beetwen goals scored and golas lost by team')
    points = models.PositiveSmallIntegerField(default=0, help_text='Enter the number of points get by team')

    class Meta:
        ordering = ['-points', '-goal_difference', 'name']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.name

class StartPosition(models.Model):
    position = models.PositiveSmallIntegerField(unique=True, help_text='Enter the position in the group at the starte')

    class Meta:
        ordering = ['position']

    def __str__(self):
        return str(self.position)

class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='group_member', blank=False, help_text='Choose the group in which the team plays in tournaments', on_delete=models.PROTECT)
    team = models.ForeignKey(Team, related_name='team_member', blank=False, help_text='Choose a team participate in the tournament', on_delete=models.PROTECT)
    position_at_start = models.ForeignKey(StartPosition, related_name='start_position_member', blank=False, help_text='Choose the position in the group at the start', on_delete=models.PROTECT)
    code_position_at_start = models.CharField(max_length=2, unique=True, editable=False)

    played = models.PositiveSmallIntegerField(default=0, help_text='Enter the number of played match by team')
    won = models.PositiveSmallIntegerField(default=0, help_text='Enter the number of won match by team')
    drawn = models.PositiveSmallIntegerField(default=0, help_text='Enter the number of drawn match by team')
    lost = models.PositiveSmallIntegerField(default=0, help_text='Enter the number of lost match by team')
    goal_for = models.PositiveSmallIntegerField(default=0, help_text='Enter the number of goals scored by team')
    goal_against = models.PositiveSmallIntegerField(default=0, help_text='Enter the number of goals lost by team')
    goal_difference = models.SmallIntegerField(default=0, help_text='Enter the difference beetwen goals scored and golas lost by team')
    points = models.PositiveSmallIntegerField(default=0, help_text='Enter the number of points get by team')

    class Meta:
        ordering = ['group', '-points', '-goal_difference', 'position_at_start']

    def save(self, *args, **kwargs):
        self.code_position_at_start = self.group.name[-1] + str(self.position_at_start)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.group.name + ' - ' + self.team.name

class GroupMatch(models.Model):
    group = models.ForeignKey(Group, related_name='group_match', blank=False, help_text='Choose the group in which the team plays in tournaments', on_delete=models.PROTECT)
    host = models.ForeignKey(GroupMember, related_name='host_group_match', blank=False, help_text='Choose a team that will be the host team', on_delete=models.PROTECT)
    guest = models.ForeignKey(GroupMember, related_name='guest_group_match', blank=False, help_text='Choose a team that will be the host guest', on_delete=models.PROTECT)
    code_group_match = models.CharField(max_length=5, unique=True, editable=False)
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(allow_unicode=True, max_length=100, unique=True, editable=False, default='')

    class Meta:
        ordering = ['date']

    def save(self, *args, **kwargs):
        self.code_group_match = slugify(self.host.code_position_at_start + '-' + self.guest.code_position_at_start)
        self.slug = self.host.team.name + '-' + self.guest.team.name
        super().save(*args, **kwargs)

    def __str__(self):
        return self.host.group.name + '/' + self.host.team.name + ' - ' + self.guest.group.name + '/' + self.guest.team.name

class GroupMatchScore(models.Model):
    group_match = models.ForeignKey(GroupMatch, related_name='score_group_match', blank=False, on_delete=models.CASCADE)
    host_goals = models.PositiveSmallIntegerField(default=0, help_text='Enter the goals for host team')
    guest_goals = models.PositiveSmallIntegerField(default=0, help_text='Enter the goals for guest team')

    class Meta:
        ordering = ['group_match']

    def __str__(self):
        return str(self.group_match)

class GroupMatchPredict(models.Model):
    user_predict = models.ForeignKey(User, related_name='user_predict_group_match', blank=False, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now, editable=False)
    group_match = models.ForeignKey(GroupMatch, related_name='predict_group_match', blank=False, on_delete=models.CASCADE)
    host_goals = models.PositiveSmallIntegerField(default=0, help_text='Enter predict number of goals for host team')
    guest_goals = models.PositiveSmallIntegerField(default=0, help_text='Enter predict number of goals for guest team')

    def __str__(self):
        return str(self.user_predict) + ": " + str(self.group_match) + " " + str(self.host_goals) + ":" + str(self.guest_goals)
