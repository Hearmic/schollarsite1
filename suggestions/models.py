from django.db import models
from users.models import User
from django.contrib.auth.models import Group


class Suggestion(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_moderated = models.BooleanField(default=False)  # Flag for moderation status
    is_denied = models.BooleanField(default=False)  # Flag for denial status
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Link to user if using authentication
    votes_for = models.IntegerField(default=0)
    max_votes_for = models.IntegerField(default=500)
    votes_against = models.IntegerField(default=0)
    max_votes_against = models.IntegerField(default=300)
    voters_for = models.ManyToManyField(User, related_name='for_suggestions', blank=True)
    voters_against = models.ManyToManyField(User, related_name='against_suggestions', blank=True)
    restricted_to_groups = models.ManyToManyField(Group, blank=True)
    denial_reason = models.CharField(max_length=100, verbose_name="Причина отказа", blank=True)

    def has_voted_for(self, user):
        return user in self.voters_for.all()

    def has_voted_against(self, user):
        return user in self.voters_against.all()

    def __str__(self):
        return self.title

    def can_vote(self, user):
        user_groups = set(user.groups.all())
        suggestion_groups = set(self.restricted_to_groups.all())
        return not suggestion_groups or user_groups.intersection(suggestion_groups)
