# Generated by Django 5.0.1 on 2024-03-26 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduprod', '0002_question_section_question_topic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='section',
            field=models.CharField(default='General', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='topic',
            field=models.CharField(choices=[('General', 'General Knowledge'), ('Maths', 'Mathematics')], default='General', max_length=200),
        ),
    ]
