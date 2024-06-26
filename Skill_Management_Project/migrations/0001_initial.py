# Generated by Django 5.0.4 on 2024-04-19 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('employeeId', models.CharField(max_length=15)),
                ('mobileNo', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('managerId', models.CharField(max_length=15)),
                ('projectId', models.CharField(max_length=15)),
            ],
        ),
    ]
