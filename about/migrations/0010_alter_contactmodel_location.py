# Generated by Django 5.1.4 on 2024-12-17 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_alter_contactmodel_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='location',
            field=models.TextField(help_text="Manzilingizni xaritada ko'rsatish uchun joylashuvni kiriting."),
        ),
    ]
