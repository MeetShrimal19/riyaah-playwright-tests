import logging, os

os.makedirs("logs", exist_ok=True)
log_path = os.path.join("logs", "test_logs.log")

logger = logging.getLogger("RiyaahLogger")
logger.setLevel(logging.INFO)
logger.propagate = False

if logger.hasHandlers():
    logger.handlers.clear()

file = logging.FileHandler(log_path, mode="a", encoding="utf-8")
file.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
logger.addHandler(file)

stream = logging.StreamHandler()
stream.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
logger.addHandler(stream)
