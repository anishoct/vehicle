# Generated by Django 4.1.5 on 2023-01-31 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tatacars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='img',
            field=models.ImageField(default='sgdshd', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
