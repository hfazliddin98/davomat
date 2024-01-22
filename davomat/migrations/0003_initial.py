# Generated by Django 5.0.1 on 2024-01-21 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('davomat', '0002_delete_guruh_delete_kurs_delete_yonalish'),
        ('users', '0008_talaba'),
    ]

    operations = [
        migrations.CreateModel(
            name='Davomat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kun', models.DateField(auto_now=True)),
                ('bor', models.BooleanField(default=False)),
                ('yoq', models.BooleanField(default=False)),
                ('amaliyot', models.BooleanField(default=False)),
                ('olinmadi', models.BooleanField(default=False)),
                ('talaba_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.talaba')),
            ],
        ),
    ]
