# Generated by Django 3.1 on 2020-09-10 08:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_post_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(default='/media/work.jpg', upload_to='')),
                ('category', models.CharField(choices=[('L', 'success'), ('UC', 'warning'), ('F', 'info')], max_length=50)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]