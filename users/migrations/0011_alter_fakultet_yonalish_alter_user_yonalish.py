# Generated by Django 5.0.1 on 2024-01-22 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_talaba_fish_talaba_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fakultet',
            name='yonalish',
            field=models.CharField(choices=[('Matematika-informatika', 'Matematika-informatika'), ('Fizika-asteranomiya', 'Fizika-asteranomiya')], default='Matematika-informatika', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='yonalish',
            field=models.CharField(choices=[('Matematika-informatika', 'Matematika-informatika'), ('Fizika-asteranomiya', 'Fizika-asteranomiya')], default='Matematika-informatika', max_length=50),
        ),
    ]