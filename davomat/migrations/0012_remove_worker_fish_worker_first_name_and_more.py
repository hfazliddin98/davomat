# Generated by Django 5.0.1 on 2024-01-30 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('davomat', '0011_remove_worker_first_name_remove_worker_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='fish',
        ),
        migrations.AddField(
            model_name='worker',
            name='first_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='last_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='worker',
            name='sharif',
            field=models.CharField(default=2, max_length=70),
            preserve_default=False,
        ),
    ]
