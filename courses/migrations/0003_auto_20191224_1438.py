# Generated by Django 3.0.1 on 2019-12-24 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20191224_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubLesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=140, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Quiz')),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='topic',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
