# Generated by Django 3.1 on 2020-09-20 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200918_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='viewsUser',
            field=models.IntegerField(default=0),
        ),
    ]
