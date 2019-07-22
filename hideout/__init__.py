# -*- coding: utf-8 -*-
import os
import glob
import pickle
from hideout import env
from hideout.log import logger
from hideout.utils import freeze


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

    def resume(self, method):
        if not self.succeeded_to_load():
            self.loaded_object = method()
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


def remove_all(base_dir=env.HIDEOUT_BASEDIR):
    files = glob.glob("{}/*.pickle".format(base_dir))
    logger.info("removing all pickles in {}".format(base_dir))
    for f in files:
        os.remove(f)
