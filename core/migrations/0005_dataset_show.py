# Generated by Django 2.0.3 on 2018-04-22 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_dataset_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]
