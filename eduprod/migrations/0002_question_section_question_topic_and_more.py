# Generated by Django 5.0.1 on 2024-03-26 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduprod', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='section',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_text',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='', max_length=200),
        ),
    ]
