# Generated by Django 2.2.7 on 2020-02-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etna_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elaqe_melumatlari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Elaqe_Sekil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Haqqimizda_melumatlari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sadalanan_melumatlar', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Haqqimizda_Sekil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Xidmetler_Sekil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
    ]
