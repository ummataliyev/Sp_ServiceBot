# Generated by Django 4.2.4 on 2023-08-17 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
        ('bot', '0002_alter_tg_users_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='from_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.province'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='where',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.district'),
        ),
    ]
