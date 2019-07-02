# -*- coding: utf-8 -*-
import os
import pickle
import contextlib
import glob
from hideout import env
from hideout.keeper import Keeper
from hideout.log import logger


@contextlib.contextmanager
def resume(file_prefix):
    file_path = "{}/{}.pickle".format(env.HIDEOUT_BASEDIR, file_prefix)
    target = Keeper(file_path)
    yield target  # run in with clause
    if target.loaded_object is not None:
        _freeze(target.loaded_object, file_path)
    else:
        raise RuntimeError("Any object is loaded...")


def _freeze(target_object, file_path):
    if not os.path.exists(file_path) or env.HIDEOUT_WITHOUT_CACHE:
        logger.info("saving {}".format(file_path))
        with open(file_path, mode='wb') as f:
            return pickle.dump(target_object, f)


def remove_all(base_dir=env.HIDEOUT_BASEDIR):
    files = glob.glob("{}/*.pickle".format(base_dir))
    for f in files:
        os.remove(f)
