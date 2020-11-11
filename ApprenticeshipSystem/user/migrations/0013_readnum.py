# Generated by Django 2.2 on 2020-11-11 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_profile_portrait'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_num', models.IntegerField(default=0)),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Teacher')),
            ],
        ),
    ]
