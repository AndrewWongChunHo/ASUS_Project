# Generated by Django 3.2.12 on 2022-04-29 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20220429_1854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelproduct',
            name='image',
        ),
        migrations.RemoveField(
            model_name='modelproduct',
            name='upload_date',
        ),
    ]
