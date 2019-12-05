# Generated by Django 2.2.5 on 2019-11-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20191101_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_contirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('krw', 'KRW'), ('usd', 'USD')], default='kr', max_length=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='langauge',
            field=models.CharField(blank=True, choices=[('kr', 'Korean'), ('en', 'English')], default='krw', max_length=2),
        ),
    ]