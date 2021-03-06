# Generated by Django 4.0.3 on 2022-04-06 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('short_description', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=600)),
                ('status', models.IntegerField(default=0)),
                ('logo', models.ImageField(upload_to='upload')),
            ],
        ),
    ]
