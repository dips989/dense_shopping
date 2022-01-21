# Generated by Django 3.2.7 on 2021-10-04 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=200)),
                ('roll_no', models.IntegerField(unique=True)),
                ('fee', models.FloatField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=150)),
                ('address', models.TextField(blank=True)),
                ('is_registered', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Student',
            },
        ),
    ]
