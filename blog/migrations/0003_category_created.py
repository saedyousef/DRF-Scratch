# Generated by Django 3.0.8 on 2020-07-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200709_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created',
            field=models.DateField(auto_now=True),
        ),
    ]