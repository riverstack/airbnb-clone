# Generated by Django 2.2.5 on 2019-11-27 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20191127_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('krw', 'KRW'), ('usd', 'USD')], default='kr', max_length=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='langauge',
            field=models.CharField(blank=True, choices=[('kr', 'Korean'), ('en', 'English')], default='krw', max_length=2),
        ),
    ]