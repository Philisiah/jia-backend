# Generated by Django 3.0.1 on 2019-12-27 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20191227_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='sublesson',
            new_name='sub_lesson',
        ),
    ]
