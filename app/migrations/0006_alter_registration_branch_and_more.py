# Generated by Django 5.0.1 on 2024-04-27 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_registration_abcnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='branch',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='registration',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='registration',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='registration',
            name='mail',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='registration',
            name='mid_name',
            field=models.CharField(max_length=30),
        ),
    ]
