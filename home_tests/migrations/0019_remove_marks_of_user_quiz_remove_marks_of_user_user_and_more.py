# Generated by Django 4.1.4 on 2023-02-01 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home_tests', '0018_remove_choice_language_remove_choice_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marks_of_user',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='marks_of_user',
            name='user',
        ),
        migrations.RenameField(
            model_name='catalog',
            old_name='question_text',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='number_of_questions',
        ),
        migrations.RemoveField(
            model_name='catalog',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='catalog',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_four',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='option_one',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_three',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='option_two',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Marks_Of_User',
        ),
    ]