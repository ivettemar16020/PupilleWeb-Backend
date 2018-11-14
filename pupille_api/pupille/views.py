from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers


class ListSubject(generics.ListCreateAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    permission_classes = [permissions.AllowAny]


class DetailSubject(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.AllowAny]

class ListTheme(generics.ListCreateAPIView):
    queryset = models.Theme.objects.all()
    serializer_class = serializers.ThemeSerializer
    permission_classes = [permissions.AllowAny]


class DetailTheme(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Theme.objects.all()
    serializer_class = ThemeSerializer
    permission_classes = [permissions.AllowAny]

class ListCard(generics.ListCreateAPIView):
    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer
    permission_classes = [permissions.AllowAny]


class DetailCard(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.AllowAny]

class ListComment(generics.ListCreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [permissions.AllowAny]


class DetailComment(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]