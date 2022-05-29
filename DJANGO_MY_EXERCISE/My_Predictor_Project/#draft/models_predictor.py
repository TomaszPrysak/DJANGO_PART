from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid

# Create your models here.

class Discipline(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='Enter discipline name')
    slug = models.SlugField(allow_unicode=True, max_length=100, unique=True, editable=False, default='')

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tournament(models.Model):
    name = models.CharField(max_length=150, unique=True, help_text='Enter tournament name')
    slug = models.SlugField(allow_unicode=True, max_length=150, unique=True, editable=False, default='')
    GENDER_TOURNAMENT = (
        ('Mens', 'Mens'),
        ('Womens', 'Womens'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_TOURNAMENT, default='Mens', blank=False, help_text='Choice tournament gender')

    class Meta:
        ordering = ['name', 'gender']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + '_' + self.gender)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name + " - " + self.gender

class Group(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='Enter group name')
    slug = models.SlugField(allow_unicode=True, max_length=100, unique=True, editable=False, default='')

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class GroupStartPosition(models.Model):
    position = models.PositiveSmallIntegerField(unique=True, help_text='Enter the position in the group at the starte')

    class Meta:
        ordering = ['position']

    def __str__(self):
        return str(self.position)

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text='Enter team name')
    slug = models.SlugField(allow_unicode=True, max_length=100, unique=True, editable=False, default='')
    GENDER_TEAM = (
        ('Mens', 'Mens'),
        ('Womens', 'Womens'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_TEAM, default='Mens', blank=False, help_text='Choice team gender')

    class Meta:
        ordering = ['name', 'gender']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + '_' + self.gender)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name + " - " + self.gender

class TournamentMember(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tournament = models.ForeignKey(Tournament, related_name='tournament_member', blank=False, help_text='Choose the tournament', on_delete=models.PROTECT)
    team = models.ForeignKey(Team, related_name='team_member', blank=False, help_text='Choose a team participate in the tournament', on_delete=models.PROTECT)
    group = models.ForeignKey(Group, related_name='group_member', blank=False, help_text='Choose the group in which the team plays in tournaments', on_delete=models.PROTECT)
    position_in_group_at_start = models.ForeignKey(GroupStartPosition, related_name='position_member_at_start', blank=False, help_text='Choose the team position in the group after the draw', on_delete=models.PROTECT)
    # slug = models.SlugField(allow_unicode=True, max_length=250, unique=True, editable=False, default='')

    class Meta:
        ordering = ['tournament', 'group', 'team']
        unique_together = ['tournament', 'team']

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.tournament.slug + '_' + self.team.slug)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.tournament.name + ' - ' + self.group.name + ' - ' + self.team.name
