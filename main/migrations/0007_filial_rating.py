# Generated by Django 4.0.3 on 2022-04-06 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_information_status_alter_information_video_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='filial',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
