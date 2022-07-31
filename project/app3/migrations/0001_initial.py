# Generated by Django 4.0.6 on 2022-07-30 12:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nutritions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(max_length=100)),
                ('calorie', models.IntegerField()),
                ('protein', models.FloatField()),
                ('carbohydrate', models.FloatField()),
                ('lipid', models.FloatField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
