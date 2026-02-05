import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="pagila",
        user="mcp_user",
        password="mcp123"
    )