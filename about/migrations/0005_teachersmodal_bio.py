# Generated by Django 5.1.4 on 2024-12-17 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_alter_aboutmodel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachersmodal',
            name='bio',
            field=models.CharField(default='', help_text='Qaysi fandan dars berishini kiriting', max_length=30),
            preserve_default=False,
        ),
    ]
