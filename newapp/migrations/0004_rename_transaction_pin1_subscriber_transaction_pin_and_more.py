# Generated by Django 4.2.1 on 2023-06-29 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_alter_subscriber_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='transaction_pin1',
            new_name='transaction_pin',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='transaction_pin2',
        ),
    ]
