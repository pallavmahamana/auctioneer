# Generated by Django 2.0.7 on 2018-07-05 06:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('start_auc_datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('end_auc_datetime', models.DateTimeField()),
            ],
        ),
    ]