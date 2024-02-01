# Generated by Django 5.0.1 on 2024-01-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('davomat', '0012_remove_worker_fish_worker_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='sharif',
        ),
        migrations.AddField(
            model_name='worker',
            name='fish',
            field=models.CharField(default=3, max_length=250),
            preserve_default=False,
        ),
    ]