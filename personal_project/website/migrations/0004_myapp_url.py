# Generated by Django 3.1.8 on 2021-05-22 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20210520_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='myapp',
            name='url',
            field=models.CharField(default='/airpollution', max_length=64),
            preserve_default=False,
        ),
    ]