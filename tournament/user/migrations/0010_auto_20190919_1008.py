# Generated by Django 2.1.7 on 2019-09-19 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_match_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name_plural': 'Matches'},
        ),
        migrations.AlterModelOptions(
            name='tournamentmodel',
            options={'verbose_name_plural': 'Tournament'},
        ),
        migrations.AlterModelOptions(
            name='usermodel',
            options={'verbose_name_plural': 'User Model'},
        ),
    ]
