# Generated by Django 4.1.4 on 2023-01-07 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_tests', '0013_alter_question_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='correct_votes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]