# Generated by Django 2.2 on 2020-11-04 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_auto_20201104_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_No',
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='enter_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
