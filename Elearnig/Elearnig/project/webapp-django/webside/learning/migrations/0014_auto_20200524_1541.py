# Generated by Django 2.2.7 on 2020-05-24 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0013_auto_20200524_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_long_overview',
            field=models.CharField(default='NULL', max_length=2000),
        ),
    ]
