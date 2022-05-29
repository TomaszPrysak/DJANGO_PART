from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils import timezone

# Create your models here.

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

    class Meta:
        ordering = ['name']

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

    class Meta:
        ordering = ['group', 'team']

    def save(self, *args, **kwargs):
        self.code_position_at_start = self.group.name[-1] + str(self.position_at_start)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.group.name + ' - ' + self.team.name
