# Generated by Django 4.1.4 on 2023-01-07 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_tests', '0012_alter_choice_choice_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
