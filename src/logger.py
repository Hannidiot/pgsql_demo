import logging

# Define your global formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Get the root logger
logger = logging.getLogger()

# Optionally, set the global log level if necessary
logger.setLevel(logging.INFO)

# Add a console handler (or any other handlers) to the root logger
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

# Now, iterate over all handlers in the root logger and set the global formatter
for handler in logger.handlers:
    handler.setFormatter(formatter)