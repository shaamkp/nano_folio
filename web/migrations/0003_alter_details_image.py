# Generated by Django 3.2.9 on 2021-12-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='image',
            field=models.FileField(upload_to='details/'),
        ),
    ]
