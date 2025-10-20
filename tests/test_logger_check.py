# tests/test_logger_check.py

from utils.loggers import logger

def test_logger_check():
    logger.info("✅ Logger is working correctly.")
    logger.warning("⚠️ This is a test warning.")
    logger.error("❌ Simulated error for testing.")
