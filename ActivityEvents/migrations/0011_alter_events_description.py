# Generated by Django 4.2.3 on 2023-10-06 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActivityEvents', '0010_alter_events_description_alter_events_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
