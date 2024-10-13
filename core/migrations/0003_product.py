# Generated by Django 5.0.4 on 2024-10-13 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
