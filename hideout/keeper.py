import os
import pickle

from hideout import env
from hideout.log import logger
from hideout.utils import freeze


class Keeper:
    def __init__(self, file_path):
        self.loaded_object = None
        if os.path.exists(file_path) and not env.HIDEOUT_WITHOUT_CACHE:
            logger.error("found {}".format(file_path))
            with open(file_path, mode='rb') as f:
                self.loaded_object = pickle.load(f)

    def set(self, target_object):
        self.loaded_object = target_object

    def get(self):
        return self.loaded_object

    def succeeded_to_load(self):
        if self.loaded_object is not None:
            return True
        return False

    def postprocess(self, file_path):
        if self.loaded_object is not None:
            logger.info("found pickled object ...")
            freeze(self.loaded_object, file_path)
        else:
            raise RuntimeError("Any object is loaded ...")
