# Generated by Django 5.0.1 on 2024-01-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_kurs_alter_user_lavozim_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Guruh',
        ),
        migrations.DeleteModel(
            name='Kurs',
        ),
        migrations.DeleteModel(
            name='Yonalish',
        ),
        migrations.AlterField(
            model_name='user',
            name='kurs',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='lavozim',
            field=models.CharField(choices=[('ADMIN', 'ADMIN'), ('TYUTR', 'TYUTR')], default='TYUTR', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='yonalish',
            field=models.CharField(choices=[('MI', 'MI'), ('FA', 'FA')], default='MI', max_length=2),
        ),
    ]
