# Generated by Django 4.2.3 on 2023-09-23 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActivityEvents', '0005_alter_events_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='image',
            field=models.ImageField(null=True, upload_to='media/images/'),
        ),
    ]