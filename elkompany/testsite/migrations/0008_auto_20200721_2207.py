# Generated by Django 2.2 on 2020-07-21 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsite', '0007_remove_tovar_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tovar',
            name='price',
            field=models.FloatField(error_messages={'required': 'Черт!'}, max_length=3, verbose_name='Цена'),
        ),
    ]
