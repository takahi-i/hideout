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
    keeper = Keeper(file_path)
    yield keeper  # run in with clause
    keeper.postprocess(file_path)


@contextlib.contextmanager
def _resume_from_keeper(keeper, file_path):
    yield keeper  # run in with clause
    keeper.postprocess(file_path)


def remove_all(base_dir=env.HIDEOUT_BASEDIR):
    files = glob.glob("{}/*.pickle".format(base_dir))
    logger.info("removing all pickles in {}".format(base_dir))
    for f in files:
        os.remove(f)
