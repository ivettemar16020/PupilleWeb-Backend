# Generated by Django 2.1.2 on 2018-11-27 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pupille', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ('card_id',)},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('creation_datetime',)},
        ),
        migrations.AlterModelOptions(
            name='theme',
            options={'ordering': ('created',)},
        ),
    ]