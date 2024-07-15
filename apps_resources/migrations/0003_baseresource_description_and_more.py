# Generated by Django 4.2.5 on 2024-07-14 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_resources', '0002_imageresource_linkresource_baseresource_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseresource',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='baseresource',
            name='related_programmes',
            field=models.CharField(blank=True, choices=[('Computer Engineering', 'Computer Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Petroleum Engineering', 'Petroleum Engineering')], max_length=255, null=True),
        ),
    ]