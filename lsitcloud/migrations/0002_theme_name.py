# Generated by Django 5.1.3 on 2024-11-19 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lsitcloud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='name',
            field=models.CharField(default='default_name', max_length=100, unique=True),
        ),
    ]