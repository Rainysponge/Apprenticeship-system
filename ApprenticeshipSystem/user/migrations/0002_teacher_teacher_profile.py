# Generated by Django 2.2 on 2020-11-03 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teacher_Profile',
            field=models.ForeignKey(default='00000', on_delete=django.db.models.deletion.DO_NOTHING, to='user.Profile'),
        ),
    ]
