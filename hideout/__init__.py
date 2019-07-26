# -*- coding: utf-8 -*-
import os
import glob
from typing import Dict, Callable

from hideout import env
from hideout.area import Keeper
from hideout.log import logger


def resume(label: str, func: Callable, func_args: Dict={}, stage: str=None) -> object:
    """
    Returns the object generated from given function and the arguments.
    When the cache file exist the the object is loaded from the cache and
    given function is not called.


    Parameters
    ----------
    label : str
        Prefix of the name of cache file for the loaded object.
    func : Callable
        Function to generate returned object, the function is called only when
        the cache file does not exist.
    func_args : Dict
        Arguments of the func. `func` is called with the values of func_args.
    stage : str
        stage of the program. This value is used when you want to specify
        the stage to skip caching.

    Returns
    -------
    Object : object
        object created by specified func and func_args. When the cache file
        exist, the object is loaded from the cache file without calling
        specified func.
    """
    return Keeper(label, stage).resume(func, func_args)


def remove_all(base_dir: str=env.HIDEOUT_BASEDIR):
    """
    Remove all cache files.

    Parameters
    ----------
    base_dir : str
        directory containing cache files

    Returns
    -------
    None : None
    """
    files = glob.glob("{}/*.pickle".format(base_dir))
    logger.info("removing all pickles in {}".format(base_dir))
    for f in files:
        os.remove(f)
