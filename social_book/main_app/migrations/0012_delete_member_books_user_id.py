# Generated by Django 5.0.2 on 2024-03-07 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_alter_customuser_cvc_alter_customuser_expiry_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.AddField(
            model_name='books',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]