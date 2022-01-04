# Generated by Django 3.2.7 on 2021-12-22 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20211222_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(blank=True, null=True)),
                ('martialStatus', models.CharField(blank=True, default='never married', max_length=50, null=True)),
                ('motherTounge', models.CharField(blank=True, max_length=50, null=True)),
                ('religion', models.CharField(blank=True, max_length=50, null=True)),
                ('caste', models.CharField(blank=True, max_length=50, null=True)),
                ('education', models.CharField(blank=True, max_length=30, null=True)),
                ('income', models.CharField(blank=True, max_length=30, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('states', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100, null=True)),
                ('languagesKnown', models.CharField(blank=True, max_length=200, null=True)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('complexion', models.CharField(max_length=100)),
                ('bloodGroup', models.CharField(max_length=100)),
                ('bodyType', models.CharField(max_length=100)),
                ('diet', models.CharField(max_length=100)),
                ('smoke', models.CharField(max_length=100)),
                ('drink', models.CharField(max_length=100)),
                ('physicallyImpaired', models.CharField(max_length=100)),
                ('dressStyle', models.CharField(max_length=100)),
                ('motherName', models.CharField(max_length=20)),
                ('motherOcuupation', models.CharField(max_length=30)),
                ('fatherName', models.CharField(max_length=20)),
                ('fatherOcuupation', models.CharField(max_length=30)),
                ('no_of_brothers', models.IntegerField()),
                ('no_of_brothers_married', models.IntegerField()),
                ('no_of_sisters', models.IntegerField()),
                ('no_of_sisters_married', models.IntegerField()),
                ('familyValue', models.CharField(max_length=20)),
                ('familyStatus', models.CharField(max_length=20)),
                ('familyType', models.CharField(max_length=20)),
                ('familyIncome', models.IntegerField()),
                ('nativeLocation', models.CharField(max_length=30)),
                ('medicalHistory', models.CharField(max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
