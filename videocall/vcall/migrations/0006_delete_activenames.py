# Generated by Django 4.1.2 on 2023-07-09 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vcall', '0005_remove_users_link_users_isactive'),
    ]

    operations = [
        migrations.DeleteModel(
            name='activenames',
        ),
    ]
