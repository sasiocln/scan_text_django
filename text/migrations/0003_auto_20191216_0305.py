# Generated by Django 3.0 on 2019-12-16 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0002_photo_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='language',
            field=models.CharField(choices=[('russian', 'rus'), ('english', 'eng'), ('kyrgyz', 'kyr')], default='eng', max_length=12),
        ),
    ]
