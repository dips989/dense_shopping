# Generated by Django 3.2.7 on 2021-10-13 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spapp', '0013_auto_20211012_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='forgot_password_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]