# Generated by Django 4.0.2 on 2022-02-08 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('admit_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=300)),
                ('address', models.CharField(default='', max_length=300)),
                ('mobile', models.CharField(default='', max_length=300)),
                ('email', models.CharField(default='', max_length=300)),
                ('image', models.ImageField(default='', upload_to='images')),
            ],
        ),
    ]