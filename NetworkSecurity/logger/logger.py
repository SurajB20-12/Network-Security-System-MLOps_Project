# import logging
# from datetime import datetime
# import os


# LOG_DIR = "logs"
# os.makedirs(LOG_DIR, exist_ok=True)

# LOG_FILE = os.path.join(LOG_DIR, "project.log")

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s | %(levelname)s | %(name)s | %(lineno)d | %(message)s",
#     handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()],
# )


# def get_logger(name: str):
#     return logging.getLogger(name)

import logging
import os
from pathlib import Path

CURRENT_FILE = Path(__file__)

PROJECT_ROOT = CURRENT_FILE.parent.parent

LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "project.log"

logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] %(levelname)s| %(pathname)s | %(filename)s | %(funcName)s | Line:%(lineno)d | %(message)s",
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()],
)


def get_logger(name: str):
    return logging.getLogger(name)
