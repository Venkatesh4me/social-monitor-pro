from loguru import logger
import sys
import os

os.makedirs("logs", exist_ok=True)

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | {message}"
)

logger.add(
    "logs/bot.log",
    rotation="5 MB",
    retention="10 days",
    level="DEBUG"
)

log = logger