# Generated by Django 4.0.2 on 2022-02-08 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Banner Image', max_length=300)),
                ('image', models.ImageField(default='', upload_to='images')),
            ],
        ),
    ]
