# Generated by Django 5.0.1 on 2024-01-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_fakultet_remove_talaba_guruh_remove_talaba_kurs_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talaba',
            name='fish',
        ),
        migrations.AddField(
            model_name='talaba',
            name='first_name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='talaba',
            name='last_name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='talaba',
            name='sharif',
            field=models.CharField(default=1, max_length=170),
            preserve_default=False,
        ),
    ]
