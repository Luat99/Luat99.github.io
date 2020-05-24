# Generated by Django 2.2.7 on 2020-05-23 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0009_auto_20200523_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='instructor_id',
            field=models.ForeignKey(default='INS01', on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to='learning.CourseInstructor'),
        ),
    ]