"""
configure logger format and output
manage log level
define configurable paths and defaults
support reproducibility through predictable setup
"""

import logging
from datetime import datetime
from pathlib import Path
import shutil


LOGS_DIR = Path("logs")
EXPORTS_DIR = Path("Exports")
LOGGER_NAME = "abnlookup"
LOG_FILE_NAME = "abnlookup.log"


def initLogging():
    """Initialize a shared file-backed logger for the application."""
    logger = logging.getLogger(LOGGER_NAME)
    if logger.handlers:
        return logger

    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    logPath = LOGS_DIR / LOG_FILE_NAME

    logger.setLevel(logging.INFO)
    logger.propagate = False

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )

    fileHandler = logging.FileHandler(logPath, encoding="utf-8")
    fileHandler.setFormatter(formatter)

    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)
    logger.info("Logging initialized at %s", logPath)
    return logger


def logEvent(event, level="info"):
    """Log a simple application event."""
    logger = initLogging()
    logMethod = getattr(logger, level.lower(), logger.info)
    logMethod(event)


def getCurrentLogPath():
    return LOGS_DIR / LOG_FILE_NAME


def exportLogFile(outputDir=EXPORTS_DIR):
    """Copy the current application log into the export directory."""
    initLogging()
    outputPath = Path(outputDir)
    outputPath.mkdir(parents=True, exist_ok=True)

    sourcePath = getCurrentLogPath()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    exportPath = outputPath / f"abnlookup_log_{timestamp}.log"
    shutil.copy2(sourcePath, exportPath)
    logEvent(f"Application log exported to {exportPath}")
    return str(exportPath)
