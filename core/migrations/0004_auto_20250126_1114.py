# Generated by Django 5.1.5 on 2025-01-26 16:14

from django.db import migrations

from makerschatbot.functions.read_sql_file import readsqlfile


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20250126_1044'),
    ]

    operations = [
        
        migrations.RunSQL(
            sql=readsqlfile('core/user/data/create_users'),  
            reverse_sql=readsqlfile('core/user/data/delete_users')  
        )
    ]
