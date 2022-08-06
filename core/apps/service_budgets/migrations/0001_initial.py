# Generated by Django 4.1 on 2022-08-06 22:02

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceBudgets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateField()),
                ('withdrawal_date', models.DateField()),
                ('delivery_team', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('withdrawal_team', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client', to='clients.client')),
            ],
        ),
    ]
