# Generated by Django 4.2.1 on 2023-05-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='img',
            name='image',
            field=models.ImageField(null=True, upload_to='imageeee'),
        ),
    ]