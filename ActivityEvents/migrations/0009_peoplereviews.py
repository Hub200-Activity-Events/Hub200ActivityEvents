# Generated by Django 4.2.3 on 2023-10-04 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActivityEvents', '0008_events_status_alter_event_registration_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]
