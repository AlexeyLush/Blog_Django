# Generated by Django 3.1 on 2020-09-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200918_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='/static/images/default_image.png', upload_to='', verbose_name='Изображение'),
        ),
    ]