# Generated by Django 4.1.4 on 2023-04-29 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRManagementSystemApp', '0002_alter_customuser_date_employment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_employment',
            field=models.DateField(blank=True, default='12-12-2020'),
        ),
    ]