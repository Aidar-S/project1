# Generated by Django 2.2 on 2020-06-29 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsite', '0003_auto_20200629_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tovar',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testsite.Category', verbose_name='Категория'),
        ),
    ]
