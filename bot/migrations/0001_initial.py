# Generated by Django 4.2.4 on 2023-08-17 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tg_Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('step', models.IntegerField(default=0)),
                ('number', models.IntegerField()),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Tg_User',
                'verbose_name_plural': 'Tg_Users',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('from_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.province')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_orders', to='bot.tg_users')),
                ('where', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.district')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
