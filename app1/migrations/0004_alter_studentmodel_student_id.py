# Generated by Django 5.0.8 on 2024-08-08 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_studentmodel_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='student_id',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
