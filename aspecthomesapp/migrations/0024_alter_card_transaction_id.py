# Generated by Django 5.0.1 on 2024-03-03 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aspecthomesapp', '0023_alter_card_expirydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='transaction_id',
            field=models.BigIntegerField(null=True),
        ),
    ]
