# Generated by Django 4.0.2 on 2022-03-02 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('induz', '0003_first_tb_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='img_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]