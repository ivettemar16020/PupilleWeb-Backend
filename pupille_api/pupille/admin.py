from django.contrib import admin

from .models import Subject, Theme, Card, Comment

admin.site.register(Subject)
admin.site.register(Theme)
admin.site.register(Card)
admin.site.register(Comment)