# Generated by Django 2.1.2 on 2018-11-27 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs_context', '0002_auto_20181118_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='post',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
