# Generated by Django 3.0.7 on 2020-06-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='title',
            field=models.CharField(default='', max_length=254),
        ),
    ]
