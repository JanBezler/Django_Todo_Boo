# Generated by Django 3.0.4 on 2020-05-22 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20200522_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
