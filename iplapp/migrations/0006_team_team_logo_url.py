# Generated by Django 3.0.14 on 2022-07-27 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iplapp', '0005_auto_20220713_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='team_logo_url',
            field=models.CharField(default='https://image.ibb.co/miF7FL/default-image.jpg', max_length=510, null=True),
        ),
    ]