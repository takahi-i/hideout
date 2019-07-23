# -*- coding: utf-8 -*-
import os
import glob

from hideout import env
from hideout.area import Keeper
from hideout.log import logger


def resume(label, func, func_args={}):
    return Keeper(label).resume(func, func_args)


def remove_all(base_dir=env.HIDEOUT_BASEDIR):
    files = glob.glob("{}/*.pickle".format(base_dir))
    logger.info("removing all pickles in {}".format(base_dir))
    for f in files:
        os.remove(f)
