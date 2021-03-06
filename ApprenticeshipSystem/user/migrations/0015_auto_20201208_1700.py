# Generated by Django 2.2 on 2020-12-08 09:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_readnum_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readnum',
            name='user',
        ),
        migrations.CreateModel(
            name='ReadDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('read_num', models.IntegerField(default=0)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Teacher')),
            ],
        ),
    ]
