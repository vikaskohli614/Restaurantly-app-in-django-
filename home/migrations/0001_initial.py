# Generated by Django 4.0.1 on 2022-03-09 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tablebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('people', models.CharField(max_length=20)),
                ('message', models.TextField()),
            ],
        ),
    ]