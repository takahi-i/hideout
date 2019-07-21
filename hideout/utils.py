import os
import pickle

from hideout import env
from hideout.log import logger


def freeze(target_object, file_path):
    if not os.path.exists(file_path) or env.HIDEOUT_WITHOUT_CACHE:
        logger.info("saving {}".format(file_path))
        with open(file_path, mode='wb') as f:
            return pickle.dump(target_object, f)
