# Generated by Django 4.2.6 on 2023-10-26 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActivityEvents', '0014_eventorganizer'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventorganizer',
            name='jobTitle',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='eventorganizer',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
