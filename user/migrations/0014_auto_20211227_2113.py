# Generated by Django 3.2.7 on 2021-12-27 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_familyinfotb_familyincome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familyinfotb',
            name='noofBrothers',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='familyinfotb',
            name='noofBrothersMarried',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='familyinfotb',
            name='noofSisters',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='familyinfotb',
            name='noofSistersMarried',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]