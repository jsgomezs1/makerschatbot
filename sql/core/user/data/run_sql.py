from django.db import migrations

from makerschatbot.functions.read_sql_file import readsqlfile
          
migrations.RunSQL(
            sql=readsqlfile('core/user/data/create_users'),  
            reverse_sql=readsqlfile('core/user/data/delete_users')  
        )