# Generated by Django 5.0.2 on 2024-03-08 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_delete_member_books_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='expiry_date',
        ),
        migrations.AddField(
            model_name='customuser',
            name='expiry_month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='expiry_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='credit_card_number',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
