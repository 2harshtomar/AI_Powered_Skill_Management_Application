# Generated by Django 5.0.4 on 2024-04-20 17:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skill_Management_Project', '0003_remove_skilldefination_certificateid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skilldefination',
            name='certificate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Certificates', to='Skill_Management_Project.certificate'),
        ),
    ]
