# Generated by Django 2.2 on 2020-11-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_profile_real_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='student_ID',
            field=models.CharField(max_length=8, null=True, verbose_name='学号'),
        ),
    ]