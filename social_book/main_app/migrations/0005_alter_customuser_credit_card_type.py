# Generated by Django 5.0.2 on 2024-03-04 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='credit_card_type',
            field=models.CharField(choices=[('Visa', 'Visa'), ('Mastercard', 'Mastercard'), ('American Express', 'American Express'), ('Discover', 'Discover')], max_length=255),
        ),
    ]
