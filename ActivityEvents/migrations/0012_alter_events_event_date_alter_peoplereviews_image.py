# Generated by Django 4.2.6 on 2023-10-26 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActivityEvents', '0011_merge_20231026_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_date',
            field=models.DateField(default=datetime.date(2023, 10, 26), null=True),
        ),
        migrations.AlterField(
            model_name='peoplereviews',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
