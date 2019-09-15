# Generated by Django 2.1.7 on 2019-09-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_ch', models.SmallIntegerField(choices=[(1, 'quarter'), (2, 'semifinal'), (3, 'final')], default=1)),
            ],
        ),
    ]
