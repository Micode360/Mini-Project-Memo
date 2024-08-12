# Generated by Django 5.0.8 on 2024-08-12 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_memo_image_alter_memo_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='memo',
            name='video',
            field=models.FileField(upload_to='videos'),
        ),
    ]
