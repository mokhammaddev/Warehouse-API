# Generated by Django 5.0.3 on 2024-03-12 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordercount',
            name='material_name',
            field=models.ManyToManyField(to='main.material'),
        ),
    ]