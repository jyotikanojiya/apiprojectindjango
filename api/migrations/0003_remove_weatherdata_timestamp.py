# Generated by Django 4.2.5 on 2024-01-21 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_weatherdata_delete_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherdata',
            name='timestamp',
        ),
    ]
