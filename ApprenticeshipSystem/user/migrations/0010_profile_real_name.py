# Generated by Django 2.2 on 2020-11-04 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_remove_teacher_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='real_name',
            field=models.CharField(max_length=10, null=True, verbose_name='真实姓名'),
        ),
    ]
