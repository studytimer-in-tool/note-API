import logging

def setup_logger():
    """
    ログ設定を行う。
    """
    logger = logging.getLogger("note-post-tool")
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger
