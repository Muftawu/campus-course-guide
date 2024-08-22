# Generated by Django 4.2.5 on 2024-08-21 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_resources', '0005_resource_resource_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='resource_link',
            field=models.URLField(blank=True, null=True, verbose_name='Resource link where applicable'),
        ),
    ]
