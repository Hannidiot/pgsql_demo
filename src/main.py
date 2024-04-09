import asyncio
import platform
import sys

from logger import logger

if ("windows" in platform.system().lower()):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

cmd = ""
if len(sys.argv) > 1:
    cmd = sys.argv[1].strip().lower()

logger.info(f"command line parameters: {' '.join(sys.argv)}")

if cmd == "" or cmd == "basic":
    from basic.run_test import run
elif cmd == "pooling":
    from pooling.run_test import run
elif cmd == "orm":
    pass
else:
    from basic.run_test import run

asyncio.run(run())