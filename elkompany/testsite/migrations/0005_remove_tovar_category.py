# Generated by Django 2.2 on 2020-06-29 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testsite', '0004_auto_20200629_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tovar',
            name='category',
        ),
    ]
