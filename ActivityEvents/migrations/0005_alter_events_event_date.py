# Generated by Django 4.2.4 on 2023-09-23 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActivityEvents', '0004_rename_gests_event_registration_guests_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_date',
            field=models.DateField(default=datetime.date(2023, 9, 23), null=True),
        ),
    ]
