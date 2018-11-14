from rest_framework import serializers
from . import models

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'subject_id',
            'name',
            'description',
            'created',
            'created_by'
        )
        model = models.Subject
        exclude = []

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Theme
        exclude = []

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Card
        exclude = []

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        exclude = []
