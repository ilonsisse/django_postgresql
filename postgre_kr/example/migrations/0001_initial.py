# Generated by Django 5.0.6 on 2024-06-05 22:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('population', models.IntegerField(verbose_name='Население')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('income_per_month', models.DecimalField(decimal_places=2, max_digits=300, verbose_name='Месячная прибыль')),
                ('supervisor', models.CharField(blank=True, max_length=64, null=True, verbose_name='Руководитель')),
                ('is_open', models.BooleanField(default=True, verbose_name='Открыт')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='example.place', verbose_name='Район')),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
            },
        ),
    ]
