# Generated by Django 4.0.4 on 2022-06-08 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LiderApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='pais',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
