# -*- coding: utf-8 -*-
import os
import pickle
import contextlib
from hideout import env, log
from hideout.log import logger


@contextlib.contextmanager
def resume(file_name):
    file_path = "{}/{}".format(env.HIDEOUT_BASEDIR, file_name)
    target = None
    if os.path.exists(file_path) and not env.HIDEOUT_FORCE_CACHE:
        logger.error("found {}".format(file_path))
        with open(file_path, mode='rb') as f:
            target = pickle.load(f)
    yield target
    if target is not None:
        freeze(target, file_name)


def freeze(target, file_name):
    file_path="{}/{}".format(env.HIDEOUT_BASEDIR, file_name)
    if (not os.path.exists(file_path)) or env.HIDEOUT_FORCE_CACHE:
        logger.info("saving {}".format(file_path))
        with open(file_path, mode='wb') as f:
            return pickle.dump(target, f)
