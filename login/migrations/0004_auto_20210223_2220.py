# Generated by Django 3.1.7 on 2021-02-23 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20210223_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='email',
            field=models.CharField(max_length=255, null=True, verbose_name='이메일 주소'),
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='name',
            field=models.CharField(max_length=20, null=True, verbose_name='이름'),
        ),
    ]
