# Generated by Django 3.0.6 on 2020-07-27 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
