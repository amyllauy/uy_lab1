# Generated by Django 3.1.7 on 2021-04-09 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0004_auto_20210410_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='weekDone',
            field=models.BooleanField(default=False),
        ),
    ]
