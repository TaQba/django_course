# Generated by Django 2.2.5 on 2022-02-02 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accessrecord',
            name='url',
        ),
        migrations.AlterField(
            model_name='accessrecord',
            name='date',
            field=models.DateField(),
        ),
    ]
