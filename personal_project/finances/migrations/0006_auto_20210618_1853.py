# Generated by Django 3.1.8 on 2021-06-18 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finances', '0005_auto_20210617_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='comment_text',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='income',
            name='comment_char',
        ),
        migrations.AddField(
            model_name='balance',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='balances', to='users.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='income',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to='users.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='outcome',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='outcome',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='outcomes', to='users.user'),
            preserve_default=False,
        ),
    ]
