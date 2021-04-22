# Generated by Django 2.2 on 2021-04-22 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('weather_f', models.FloatField()),
                ('weather_c', models.FloatField()),
                ('weather_t', models.CharField(max_length=255)),
                ('weather_i', models.URLField()),
                ('weather_h', models.FloatField()),
            ],
        ),
    ]
