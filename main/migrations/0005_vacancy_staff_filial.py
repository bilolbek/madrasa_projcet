# Generated by Django 4.0.3 on 2022-04-06 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_information_prize_staff_alter_course_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=600)),
                ('status', models.IntegerField(default=0)),
                ('logo', models.ImageField(blank=True, upload_to='upload')),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='filial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.filial'),
            preserve_default=False,
        ),
    ]
