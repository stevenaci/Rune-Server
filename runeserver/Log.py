import sys
import os
import logging

from runeserver.utilities.file_storage import touch_folder

_LOGGER = None
LOG_LEVEL = logging.DEBUG
LOGGER_NAME = "Runeserver 1.0"

print("LOG PY TEST DIR: " + os.getcwd())
print(sys.path[0])
# creates log dir if it doesn't exist
touch_folder("./logs")

LOGGING_PATH = "logs/Runeserver.txt"
# Make a level that will always print
logging.ALWAYS = 100
logging.addLevelName(logging.ALWAYS, "ALWAYS")

def init_logger():
    global _LOGGER
    _LOGGER = logging.getLogger(LOGGER_NAME)

    if not _LOGGER.handlers:
        fmt = "{asctime} | {module} | {levelname} ||| {message}"
        fmtr = logging.Formatter(fmt=fmt, style="{")
        strm_handler = logging.StreamHandler(sys.stdout)

        strm_handler.setLevel(LOG_LEVEL)
        strm_handler.setFormatter(fmtr)

        # See if file exists. If not, create it:
        file_exists = os.path.isfile(LOGGING_PATH)
        if not file_exists:
            f = open(LOGGING_PATH, 'w')
            f.close()

        # file_handler = logging.FileHandler(LOGGING_PATH, mode='w')
        file_handler = logging.FileHandler(LOGGING_PATH, mode='a')
        file_handler.setLevel(logging.DEBUG)  # Always log to file
        file_handler.setFormatter(fmtr)

        _LOGGER.addHandler(strm_handler)
        _LOGGER.addHandler(file_handler)
    _LOGGER.setLevel(LOG_LEVEL)

def ALWAYS(msg):
    __log(msg, logging.ALWAYS)

def FATAL(msg):
    __log(msg, logging.CRITICAL)

def CRITICAL(msg):
    __log(msg, logging.CRITICAL)

def ERROR(msg):
    __log(msg, logging.ERROR)

def WARN(msg):
    __log(msg, logging.WARNING)

def WARNING(msg):
    __log(msg, logging.WARNING)

def INFO(msg):
    __log(msg, logging.INFO)

def DEBUG(msg):
    __log(msg, logging.DEBUG)

def __log(msg, msg_level):
    global _LOGGER
    if _LOGGER is None:
        init_logger()

    if _LOGGER:
        _LOGGER.log(msg_level, msg)
    else:
        raise Exception("Logger was not initialized")