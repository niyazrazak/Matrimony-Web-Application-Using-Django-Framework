# Generated by Django 3.2.7 on 2021-12-26 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffadmin', '0004_delete_happystories'),
    ]

    operations = [
        migrations.CreateModel(
            name='HappyStories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('caption', models.TextField()),
            ],
        ),
    ]