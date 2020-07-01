# Generated by Django 2.2 on 2020-06-29 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsite', '0005_remove_tovar_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovar',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='testsite.Category', verbose_name='Категория'),
        ),
    ]
