# Generated by Django 3.1.7 on 2021-06-06 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aktualnosci', '0007_auto_20210606_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wniosek',
            name='zrodlo',
            field=models.CharField(max_length=30),
        ),
    ]
