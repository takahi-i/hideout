# -*- coding: utf-8 -*-
import os
import pickle
import contextlib
from hideout import env, log
from hideout.keeper import Keeper
from hideout.log import logger


@contextlib.contextmanager
def resume(file_name):
    file_path = "{}/{}".format(env.HIDEOUT_BASEDIR, file_name)
    target = Keeper(file_path)
    yield target
    if target.object is not None:
        freeze(target, file_name)


def freeze(target, file_name):
    file_path="{}/{}".format(env.HIDEOUT_BASEDIR, file_name)
    if (not os.path.exists(file_path)) or env.HIDEOUT_FORCE_CACHE:
        logger.info("saving {}".format(file_path))
        with open(file_path, mode='wb') as f:
            return pickle.dump(target, f)
