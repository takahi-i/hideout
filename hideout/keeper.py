import os
import pickle

from hideout import env
from hideout.log import logger


class Keeper:
    def __init__(self, file_path):
        self.object = None
        if os.path.exists(file_path) and not env.HIDEOUT_FORCE_CACHE:
            logger.error("found {}".format(file_path))
            with open(file_path, mode='rb') as f:
                self.object = pickle.load(f)

    def set(self, object):
        self.object = object

    def get(self):
        return self.object

    def failed_to_load(self):
        if self.object is None:
            return True
        return False
