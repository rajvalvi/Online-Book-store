# Generated by Django 5.0.2 on 2024-03-06 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_rename_discription_books_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='CVC',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='credit_card_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='credit_card_type',
            field=models.CharField(blank=True, choices=[('Visa', 'Visa'), ('Mastercard', 'Mastercard'), ('American Express', 'American Express'), ('Discover', 'Discover')], max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='expiry_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='state',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]