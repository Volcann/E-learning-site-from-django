# Generated by Django 5.1.5 on 2025-01-25 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_course_lecture_successmetric_successstory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='course',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Lecture',
        ),
    ]
