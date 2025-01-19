import logging


class Logger:
    """
    Logger Functionality
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
    logger: logging.Logger = logging.getLogger(__name__)
