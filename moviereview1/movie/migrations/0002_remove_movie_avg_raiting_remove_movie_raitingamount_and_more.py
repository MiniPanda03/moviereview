# Generated by Django 4.1.4 on 2022-12-19 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='Avg_raiting',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='raitingAmount',
        ),
        migrations.AddField(
            model_name='movie',
            name='Actor_id',
            field=models.ManyToManyField(to='movie.actor'),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Director_id',
        ),
        migrations.DeleteModel(
            name='Actors',
        ),
        migrations.AddField(
            model_name='movie',
            name='Director_id',
            field=models.ManyToManyField(to='movie.director'),
        ),
    ]
