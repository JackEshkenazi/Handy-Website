# Generated by Django 3.0.6 on 2020-06-22 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
            preserve_default=False,
        ),
    ]