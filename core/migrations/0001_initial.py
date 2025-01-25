from django.db import migrations
from makerschatbot.functions.read_sql_file import readsqlfile

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    
    operations = [
        migrations.RunSQL(
            sql=readsqlfile('schemas/create_schemas'),  # Fix typo "shemas" → "schemas"
            reverse_sql=readsqlfile('schemas/drop_schemas')  # Fix typo here too
        )
    ]