import asyncio
import platform

from basic_usage import run as run_basic

if ("windows" in platform.system().lower()):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.run(run_basic())