# Generated by Django 4.2.3 on 2023-09-23 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActivityEvents', '0007_alter_events_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
