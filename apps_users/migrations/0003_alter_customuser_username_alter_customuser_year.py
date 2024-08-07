# Generated by Django 4.2.5 on 2024-07-12 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_users', '0002_customuser_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='year',
            field=models.CharField(blank=True, choices=[('1st Year', '1st Year'), ('2nd Year', '2nd Year'), ('3rd Year', '3rd Year'), ('4th Year', '4th Year'), ('5th Year', '5th Year'), ('6th Year', '6th Year'), ('Completed', 'Completed')], max_length=255, null=True),
        ),
    ]
