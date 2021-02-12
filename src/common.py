import sys
from sqlalchemy.ext.declarative import declarative_base
from loguru import logger

LOGGER_FORMAT = "<green>{time}</green> <level>{message}</level>"

logger.remove()
logger.add(sys.stdout, colorize=True, format=LOGGER_FORMAT)

Base = declarative_base()