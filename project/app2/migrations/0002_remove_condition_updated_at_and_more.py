# Generated by Django 4.0.6 on 2022-07-29 14:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='condition',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='condition',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]