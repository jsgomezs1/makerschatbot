# imports to make db calls

def call_db(query, params=None):
    return []

def format_query_result(result):
    formatted_result = []
    for row in result:
        # Here we change the format of the query result to match what we want the model to consume.
        formatted_result.append({
            'product_name': row[0],
            'quantity': row[1],
        })
    return formatted_result

def get_inventory():
    result = call_db
    return format_query_result(result)
