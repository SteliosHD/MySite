# Generated by Django 3.1 on 2020-09-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_remove_post_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='icon',
            field=models.CharField(default='star', max_length=40),
            preserve_default=False,
        ),
    ]