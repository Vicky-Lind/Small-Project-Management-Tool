# Generated by Django 5.0.3 on 2024-03-18 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_task_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
