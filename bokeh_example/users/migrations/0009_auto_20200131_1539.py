# Generated by Django 2.2.6 on 2020-01-31 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_auto_20200131_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamcreation',
            name='members',
            field=models.ManyToManyField(default='', related_name='Members', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teamcreation',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]