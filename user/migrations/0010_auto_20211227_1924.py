# Generated by Django 3.2.7 on 2021-12-27 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20211227_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicalinfotb',
            name='bloodGroup',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='physicalinfotb',
            name='bodyType',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='physicalinfotb',
            name='complexion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='physicalinfotb',
            name='diet',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='physicalinfotb',
            name='dressStyle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='physicalinfotb',
            name='drink',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='physicalinfotb',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='physicalinfotb',
            name='physicallyImpaired',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='physicalinfotb',
            name='smoke',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='physicalinfotb',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]