# Generated by Django 2.2.1 on 2019-05-25 19:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0003_auto_20190525_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='forum',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
