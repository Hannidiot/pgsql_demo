import psycopg

from contextlib import contextmanager, asynccontextmanager
from static import connection_string

@contextmanager
def get_connection_and_cursor():
    connection = None
    cursor = None
    try:
        connection = psycopg.connect(connection_string, row_factory=psycopg.rows.dict_row)
        cursor = connection.cursor()
        
        yield connection, cursor
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
        
@asynccontextmanager
async def get_async_connection_and_cursor():
    conn = None
    cur = None
    try:
        # Connect to the database asynchronously
        conn = await psycopg.AsyncConnection.connect(connection_string, row_factory=psycopg.rows.dict_row)
        # Create a cursor
        cur = conn.cursor()

        yield conn, cur
    finally:
        # Close the cursor and connection
        if cur is not None:
            await cur.close()
        if conn is not None:
            await conn.close()