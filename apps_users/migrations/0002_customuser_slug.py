# Generated by Django 4.2.5 on 2024-07-03 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]