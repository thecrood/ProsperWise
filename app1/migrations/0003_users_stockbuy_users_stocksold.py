# Generated by Django 5.0.4 on 2024-04-08 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_users_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='stockbuy',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='users',
            name='stocksold',
            field=models.JSONField(default=list),
        ),
    ]
