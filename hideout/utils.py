import pickle

from hideout import env
from hideout.log import logger


def freeze(target_object, file_path):
    if not env.HIDEOUT_ENABLE_CACHE:
        logger.info("skip saving to cache file ...")
        return
    logger.info("saving {}".format(file_path))
    with open(file_path, mode='wb') as f:
        return pickle.dump(target_object, f)
