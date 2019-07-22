# -*- coding: utf-8 -*-
import os
import glob

from hideout import env
from hideout.log import logger
from hideout.utils import freeze


def _generate_file_path(file_prefix):
    return "{}/{}.pickle".format(env.HIDEOUT_BASEDIR, file_prefix)


def remove_all(base_dir=env.HIDEOUT_BASEDIR):
    files = glob.glob("{}/*.pickle".format(base_dir))
    logger.info("removing all pickles in {}".format(base_dir))
    for f in files:
        os.remove(f)
