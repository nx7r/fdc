# Generated by Django 4.1.2 on 2022-10-19 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_member_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='username',
        ),
        migrations.AlterField(
            model_name='member',
            name='univ_fac',
            field=models.CharField(max_length=90, null=True),
        ),
    ]
