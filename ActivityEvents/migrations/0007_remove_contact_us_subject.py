# Generated by Django 4.2.4 on 2023-10-03 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ActivityEvents', '0006_contact_us'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_us',
            name='subject',
        ),
    ]
