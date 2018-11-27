from django.db import models
from users.models import CustomUser
 
class Subject(models.Model):
    subject_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=False, blank=False, null=False)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, related_name='subjects', on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        """A string representation of the model."""
        return self.name

class Theme(models.Model):
    themes_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=False, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    commentary = models.ManyToManyField(CustomUser, through= 'Comment', related_name='comment')

    class Meta:
        ordering = ('created',)

    def __str__(self):
        """A string representation of the model."""
        return self.name

class Card(models.Model):
    card_id = models.IntegerField(primary_key=True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    question = models.CharField(max_length=100, blank=False, null=False)
    answer = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        ordering = ('card_id',)

    def __str__(self):
        """A string representation of the model."""
        return self.theme


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, related_name='created_by', on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, related_name='theme', on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False)
    creation_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('creation_datetime',)

    def __str__(self):
        """A string representation of the model."""
        return self.user

