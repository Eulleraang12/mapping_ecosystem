# Generated by Django 2.2.11 on 2020-03-21 03:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastro', '0002_auto_20200319_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
