# Generated by Django 4.0.6 on 2022-10-11 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('participent_name', models.CharField(max_length=100)),
                ('participent_address', models.CharField(max_length=100)),
            ],
        ),
    ]
