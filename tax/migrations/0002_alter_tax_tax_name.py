# Generated by Django 3.2.9 on 2021-11-20 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tax',
            name='tax_name',
            field=models.CharField(max_length=200),
        ),
    ]
