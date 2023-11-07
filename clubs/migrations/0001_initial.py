# Generated by Django 4.2.7 on 2023-11-03 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('region', models.TextField()),
                ('district', models.TextField()),
                ('ward', models.TextField()),
                ('street', models.TextField()),
                ('reg_number', models.TextField()),
                ('icon', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]