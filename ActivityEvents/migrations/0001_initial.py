# Generated by Django 4.2.4 on 2023-09-19 12:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('event_date', models.DateField(default=datetime.date(2023, 9, 19), null=True)),
                ('location', models.CharField(max_length=50)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ActivityEvents.user')),
            ],
        ),
        migrations.CreateModel(
            name='Event_registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('gests', models.IntegerField()),
                ('comment', models.CharField(max_length=50)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ActivityEvents.events')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ActivityEvents.user')),
            ],
        ),
    ]