from django.contrib import admin

from .models import Subject, Theme, Card, Comment

from guardian.admin import GuardedModelAdmin

# With object permissions support
class AuthorAdmin(GuardedModelAdmin):
    pass

admin.site.register(Subject)
admin.site.register(Theme)
admin.site.register(Card)
admin.site.register(Comment)    