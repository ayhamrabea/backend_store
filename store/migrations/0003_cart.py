# Generated by Django 5.1.3 on 2024-11-22 21:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('store', '0002_alter_auther_bio_alter_auther_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.JSONField(default=dict)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessions.session')),
            ],
            options={
                'verbose_name': 'cart',
                'verbose_name_plural': 'carts',
            },
        ),
    ]
