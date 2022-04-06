# Generated by Django 4.0.3 on 2022-04-06 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('status', models.IntegerField(default=0)),
                ('adress', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=300)),
                ('instagram', models.CharField(blank=True, max_length=300)),
                ('whatsapp', models.CharField(blank=True, max_length=300)),
                ('email', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]
