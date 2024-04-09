import psycopg
import psycopg_pool

from contextlib import contextmanager, asynccontextmanager
from static import connection_string

# Synchronous connection pool setup
sync_pool = psycopg_pool.ConnectionPool(conninfo=connection_string, open=False, min_size=1, max_size=10)

@contextmanager
def get_connection_and_cursor():
    connection = None
    cursor = None
    try:
        # Acquire a connection from the pool
        connection = sync_pool.getconn()
        connection.row_factory = psycopg.rows.dict_row
        cursor = connection.cursor()
        
        yield connection, cursor
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            # Release the connection back to the pool instead of closing it
            sync_pool.putconn(connection)

# Asynchronous connection pool setup
async_pool = psycopg_pool.AsyncConnectionPool(conninfo=connection_string, open=False, min_size=1, max_size=10)

@asynccontextmanager
async def get_async_connection_and_cursor():
    conn = None
    cur = None
    try:
        # Acquire a connection from the asynchronous pool
        conn = await async_pool.getconn()
        conn.row_factory = psycopg.rows.dict_row
        cur = conn.cursor()

        yield conn, cur
    finally:
        if cur is not None:
            await cur.close()
        if conn is not None:
            # Release the connection back to the pool instead of closing it
            await async_pool.putconn(conn)
