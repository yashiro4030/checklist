# Generated by Django 3.2.6 on 2021-09-07 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chekslst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('systeme', models.CharField(max_length=100, null=True)),
                ('service', models.CharField(max_length=100, null=True)),
                ('checked', models.CharField(max_length=100, null=True)),
                ('action', models.TextField(max_length=500, null=True)),
                ('Remarque', models.TextField(max_length=500, null=True)),
            ],
        ),
    ]
