from psycopg import AsyncCursor
from utils import get_async_connection_and_cursor
from static import test_employee

async def run():
    async with get_async_connection_and_cursor() as (_, cursor):
        # await test_select(cursor)
        # await check_existence(cursor, False)
        await test_insert(cursor)
        # await check_existence(cursor, True)
        
    print("test success")
            
async def test_select(cur: AsyncCursor):
    get_top10_employees = "select * from employees.employees order by emp_no DESC LIMIT 10"
    await cur.execute(get_top10_employees)
    async for emp in cur:
        print(emp)
        
async def test_insert(cur: AsyncCursor):
    query = "INSERT into employees.employees (emp_no, birth_date, first_name, last_name, gender, hire_date) VALUES (%s, %s, %s, %s, %s, %s)"
    await cur.execute(query, (test_employee["emp_no"], test_employee["birth_date"], test_employee["first_name"], test_employee["last_name"], test_employee["gender"], test_employee["hire_date"]))

async def test_update(cur: AsyncCursor):
    pass

async def test_delete(cur: AsyncCursor):
    pass

async def check_existence(cur: AsyncCursor, is_exist: bool):
    query = "select * from employees.employees where first_name = %s"
    await cur.execute(query, (test_employee["first_name"],))
    emp = await cur.fetchone()
    if ((emp is not None) != is_exist):
        print(f'check_existence is not as expected')
