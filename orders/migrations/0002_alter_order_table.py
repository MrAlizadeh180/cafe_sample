# Generated by Django 4.0.1 on 2022-01-26 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='tables.table', verbose_name='Table'),
        ),
    ]
