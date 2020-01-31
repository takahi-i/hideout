# -*- coding: utf-8 -*-
import os
import glob
import hideout.log

from logging import Logger
from typing import Dict, Callable

from hideout import env
from hideout.area import Keeper
from hideout.log import logger


def resume_or_generate(
        func: Callable, func_args: Dict = {}, stage: str = None, label: str = None) -> object:
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
    return Keeper(stage=stage).resume_or_generate(
        func=func,
        func_args=func_args,
        label=label)


def resumable(stage: str = None, label: str = None):
    """
    A decorator function which returns the object generated from given function and the arguments.
    When the cache file exist the the object is loaded from the cache and
    given function is not called.

    Parameters
    ----------
    stage : str
        stage of the program. This value is used when you want to specify
        the stage to skip caching.
    label : str
        Prefix of the name of cache file for the loaded object.

    Returns
    -------
    Function: which wrap the argument function for caching.
    """
    def _memorize(function):
        def _memorized(*args, **kwargs):
            return Keeper(stage=stage).resume_or_generate_for_decorator(
                func=function,
                args=args,
                kwargs=kwargs,
                label=label)
        return _memorized
    return _memorize


def remove_all(base_dir: str = env.HIDEOUT_CACHE_DIR):
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


def set_logger(logger: Logger):
    """
    Set logger object.

    Parameters
    ----------
    logger : Logger
        Logger object

    Returns
    -------
    None
    """
    hideout.log.logger = logger
