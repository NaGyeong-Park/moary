# Generated by Django 3.2.12 on 2022-06-10 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20220610_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='poster',
        ),
    ]
