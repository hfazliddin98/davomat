# Generated by Django 5.0.1 on 2024-01-20 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_kurs_alter_user_yonalish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='kurs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.kurs'),
        ),
        migrations.AlterField(
            model_name='user',
            name='yonalish',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.yonalish'),
        ),
    ]
