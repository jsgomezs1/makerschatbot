import os

def readsqlfile(sql_filename):
    """
    Reads the content of a SQL file located in the 'sql/' directory of the Django project.
    Appends '.sql' to the filename if not already present.
    """
    project_directory = os.getcwd()
    sql_directory = os.path.join(project_directory, 'sql')

    # Append .sql if missing
    if not sql_filename.endswith('.sql'):
        sql_filename += '.sql'

    sql_file_path = os.path.join(sql_directory, sql_filename)

    try:
        with open(sql_file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"SQL file not found: {sql_file_path}")  # Raise instead of returning string
    except Exception as e:
        raise RuntimeError(f"Error reading SQL file: {e}")  # Raise proper exception