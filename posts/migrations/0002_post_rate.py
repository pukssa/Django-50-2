# Generated by Django 5.1.7 on 2025-03-13 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rate',
            field=models.IntegerField(null=True),
        ),
    ]
