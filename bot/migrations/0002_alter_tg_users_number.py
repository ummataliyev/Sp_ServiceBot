# Generated by Django 4.2.4 on 2023-08-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tg_users',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
