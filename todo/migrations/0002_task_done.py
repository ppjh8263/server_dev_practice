# Generated by Django 3.1.7 on 2021-03-04 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False, verbose_name='상태'),
        ),
    ]
