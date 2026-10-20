import logging
import functools

logging.basicConfig(
    level=logging.INFO,
    format = "%(asctime)s | %(levelname)s | %(message)s",
    handlers = [
        logging.FileHandler("app.log",encoding = "utf-8"),
        logging.StreamHandler(),
    ]
)

log = logging.getLogger("AskAtchaya")

def log_step(func):
    """ Logs whether a fuction is completed successfully or not."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            log.info("%s completed successfully.", func.__name__)
            return result
        except Exception as e:
            log.error("%s failed with error: %s", func.__name__, str(e))
            raise
    return wrapper
