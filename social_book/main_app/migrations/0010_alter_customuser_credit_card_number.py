# Generated by Django 5.0.2 on 2024-03-06 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_customuser_cvc_alter_customuser_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='credit_card_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
