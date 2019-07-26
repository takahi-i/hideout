import os
import pickle
from typing import Callable, Dict

from hideout import env
from hideout.utils import freeze
from hideout.log import logger


def _generate_file_path(file_prefix):
    return "{}/{}.pickle".format(env.HIDEOUT_BASEDIR, file_prefix)


class Keeper:
    def __init__(self, file_prefix: str, stage: str=None):
        self.file_path = _generate_file_path(file_prefix)
        self.stage = stage
        self.loaded_object = None
        if not env.HIDEOUT_ENABLE_CACHE or stage in env.HIDEOUT_SKIP_STAGES:
            logger.error("suppressed loading cache")
            return
        if os.path.exists(self.file_path):
            logger.error("found {}".format(self.file_path))
            with open(self.file_path, mode='rb') as f:
                self.loaded_object = pickle.load(f)

    def resume(self, func: Callable, func_args: Dict) -> object:
        if not self.succeeded_to_load():
            if len(func_args) == 0:
                self.loaded_object = func()
            else:
                self.loaded_object = func(**func_args)
            self.postprocess()
        return self.loaded_object

    def set(self, target_object: object) -> None:
        self.loaded_object = target_object

    def get(self) -> object:
        return self.loaded_object

    def succeeded_to_load(self) -> bool:
        if self.loaded_object is not None:
            return True
        return False

    def postprocess(self) -> None:
        if self.loaded_object is not None:
            logger.info("found pickled object ...")
            freeze(self.loaded_object, self.file_path, self.stage)
        else:
            raise RuntimeError("Any object is loaded ...")
