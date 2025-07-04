# see https://python-bloggers.com/2024/04/logging-like-a-lumberjack/
import logging
from logging import debug, info, warning, error
from datetime import datetime

FMT_MESSAGE = "%(asctime)s [wp2 %(levelname)7s] %(message)s"
FMT_DATETIME = "%Y-%m-%d %H:%M:%S"

# Get default logger.
logger = logging.getLogger()

# Set logging level.
logger.setLevel(logging.INFO)

formatter = logging.Formatter(FMT_MESSAGE, datefmt=FMT_DATETIME)

# Logging to console.
console = logging.StreamHandler()
console.setFormatter(formatter)
logger.addHandler(console)

# Logging to file.
#
file = logging.FileHandler(datetime.now().strftime("wp2_%Y%m%d-%H%M%S.log"))
file.setFormatter(formatter)
logger.addHandler(file)
