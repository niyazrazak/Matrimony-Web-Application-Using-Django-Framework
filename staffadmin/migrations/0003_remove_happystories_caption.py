# Generated by Django 3.2.7 on 2021-12-26 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staffadmin', '0002_happystories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='happystories',
            name='caption',
        ),
    ]
