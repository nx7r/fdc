# Generated by Django 4.1.2 on 2022-11-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_event_participents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='participents',
            field=models.ManyToManyField(blank=True, to='events.participent'),
        ),
    ]
