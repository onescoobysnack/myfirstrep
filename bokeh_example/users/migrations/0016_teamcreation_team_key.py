# Generated by Django 2.2.6 on 2020-02-07 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_teamcreation_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamcreation',
            name='team_key',
            field=models.CharField(default='enter a team key', max_length=80, unique=True),
        ),
    ]
