# Generated by Django 4.1 on 2022-08-15 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('users', '0003_remove_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='profile', to='profiles.profile'),
            preserve_default=False,
        ),
    ]