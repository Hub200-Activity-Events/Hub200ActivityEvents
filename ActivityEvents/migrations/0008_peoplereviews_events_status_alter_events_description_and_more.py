# Generated by Django 4.2.3 on 2023-10-06 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActivityEvents', '0007_remove_contact_us_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_date',
            field=models.DateField(default=datetime.date(2023, 10, 6), null=True),
        ),
    ]
