# Generated by Django 3.2.7 on 2021-10-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spapp', '0003_contact_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='contact_number',
            field=models.IntegerField(blank=True),
        ),
    ]