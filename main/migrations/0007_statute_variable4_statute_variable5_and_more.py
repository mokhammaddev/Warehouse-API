# Generated by Django 5.0.3 on 2024-03-12 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_statute'),
    ]

    operations = [
        migrations.AddField(
            model_name='statute',
            name='variable4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statute',
            name='variable5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='statute',
            name='variable6',
            field=models.IntegerField(default=0),
        ),
    ]