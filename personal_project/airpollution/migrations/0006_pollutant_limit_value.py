# Generated by Django 3.1.8 on 2021-06-02 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airpollution', '0005_auto_20210602_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollutant',
            name='limit_value',
            field=models.SmallIntegerField(null=True),
        ),
    ]
