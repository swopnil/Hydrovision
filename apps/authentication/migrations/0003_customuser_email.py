# Generated by Django 3.2.11 on 2024-07-22 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20240722_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
    ]
