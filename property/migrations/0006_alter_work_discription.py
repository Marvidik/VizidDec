# Generated by Django 4.1 on 2023-06-14 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_work_pictures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='discription',
            field=models.TextField(),
        ),
    ]