# Generated by Django 2.2 on 2020-11-08 13:01

from django.db import migrations, models
import user.tools


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_profile_student_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='portrait',
            field=models.ImageField(blank=True, null=True, upload_to=user.tools.user_directory_path, verbose_name='头像'),
        ),
    ]
