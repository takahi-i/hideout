import os
import pickle

from hideout import logger, env


class Keeper:

    def __init__(self, file_path):
        self.object = None
        if os.path.exists(file_path) and not env.HIDEOUT_FORCE_CACHE:
            logger.error("found {}".format(file_path))
            with open(file_path, mode='rb') as f:
                self.object = pickle.load(f)
