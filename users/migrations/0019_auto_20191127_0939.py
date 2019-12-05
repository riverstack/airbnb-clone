# Generated by Django 2.2.5 on 2019-11-27 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20191127_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('email', 'Email'), ('github', 'Github'), ('kakao', 'Kakao')], default='kakao', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('usd', 'USD'), ('krw', 'KRW')], default='kr', max_length=3),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('female', 'Female'), ('other', 'Other'), ('male', 'Male')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='langauge',
            field=models.CharField(blank=True, choices=[('en', 'English'), ('kr', 'Korean')], default='krw', max_length=2),
        ),
    ]