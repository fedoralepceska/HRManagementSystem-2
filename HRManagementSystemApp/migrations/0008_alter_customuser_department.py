# Generated by Django 4.1.4 on 2023-04-29 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HRManagementSystemApp', '0007_alter_customuser_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foreignDepartment', to='HRManagementSystemApp.department'),
        ),
    ]
