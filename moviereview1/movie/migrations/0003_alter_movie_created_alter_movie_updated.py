# Generated by Django 4.1.4 on 2023-01-14 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_rating_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
