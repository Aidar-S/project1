# Generated by Django 2.2 on 2020-07-21 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testsite', '0006_tovar_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tovar',
            name='category',
        ),
    ]