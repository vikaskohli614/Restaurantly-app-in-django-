# Generated by Django 4.0.1 on 2022-03-09 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contactus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='name',
            new_name='cname',
        ),
    ]