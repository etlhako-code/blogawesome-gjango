# Generated by Django 2.2.4 on 2020-03-25 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200325_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Unspecified', max_length=100),
        ),
    ]