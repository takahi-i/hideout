# -*- coding: utf-8 -*-
import os
import contextlib
import glob
from hideout import env
from hideout.keeper import Keeper
from hideout.log import logger


@contextlib.contextmanager
def resume(file_prefix):
    keeper = Keeper(file_prefix)
    yield keeper  # run in with clause
    keeper.postprocess()


@contextlib.contextmanager
def _resume_from_keeper(keeper):
    yield keeper  # run in with clause
    keeper.postprocess()


def remove_all(base_dir=env.HIDEOUT_BASEDIR):
    files = glob.glob("{}/*.pickle".format(base_dir))
    logger.info("removing all pickles in {}".format(base_dir))
    for f in files:
        os.remove(f)
