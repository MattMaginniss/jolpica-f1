# Generated by Django 3.2.6 on 2021-08-07 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ergast', '0006_auto_20210807_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptimes',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Unique id from foreign key concatenation'),
        ),
        migrations.AlterField(
            model_name='pitstops',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Unique id from foreign key concatenation'),
        ),
    ]
