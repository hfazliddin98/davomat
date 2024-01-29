# Generated by Django 5.0.1 on 2024-01-24 16:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('davomat', '0005_fakultet_guruh_kurs_yonalish_alter_davomat_fakultet_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guruh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='davomat.guruh')),
                ('kurs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='davomat.kurs')),
                ('yonalish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='davomat.yonalish')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='davomat.team')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=70)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='davomat.team')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_attended', models.BooleanField(default=False)),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='davomat.attendance')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='davomat.worker')),
            ],
            options={
                'unique_together': {('attendance', 'worker')},
            },
        ),
    ]
