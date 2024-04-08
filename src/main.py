import asyncio

from basic_usage import run as run_basic

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(run_basic())