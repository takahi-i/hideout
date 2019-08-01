from logging import getLogger, StreamHandler, INFO
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(INFO)
logger.setLevel(INFO)
logger.addHandler(handler)
logger.propagate = False
