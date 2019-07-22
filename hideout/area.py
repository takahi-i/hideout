import os
import pickle

from hideout import env
from hideout.utils import freeze
from hideout.log import logger


def _generate_file_path(file_prefix):
    return "{}/{}.pickle".format(env.HIDEOUT_BASEDIR, file_prefix)


class Keeper:
    def __init__(self, file_prefix):
        self.file_path = _generate_file_path(file_prefix)
        self.loaded_object = None
        if os.path.exists(self.file_path) and not env.HIDEOUT_WITHOUT_CACHE:
            logger.error("found {}".format(self.file_path))
            with open(self.file_path, mode='rb') as f:
                self.loaded_object = pickle.load(f)

    def resume(self, func, **kwargs):
        if not self.succeeded_to_load():
            if len(kwargs) == 0:
                self.loaded_object = func()
            else:
                self.loaded_object = func(**kwargs)
            self.postprocess()
        return self.loaded_object

    def set(self, target_object):
        self.loaded_object = target_object

    def get(self):
        return self.loaded_object

    def succeeded_to_load(self):
        if self.loaded_object is not None:
            return True
        return False

    def postprocess(self):
        if self.loaded_object is not None:
            logger.info("found pickled object ...")
            freeze(self.loaded_object, self.file_path)
        else:
            raise RuntimeError("Any object is loaded ...")
