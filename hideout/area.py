import os
import pickle
from typing import Callable, Dict

from hideout import env
from hideout.file import freeze, generate_path
from hideout.log import logger


class Keeper:
    """
    Load and save the given object
    """

    def __init__(self, stage: str = None):
        """
        Constructor.

        Parameters
        ----------
        stage : str
            Stage of program.
        """
        self.stage = stage

    def resume(self, func: Callable, func_args: Dict, label: str = None) -> object:
        """
        Returns the object generated from func with func_args parameters. When exist cache file
        resume method does not given func and load the object from cache file.

        Parameters
        ----------
        func : Callable
            function to generate result object
        func_args : Dict
            parameters of the func.
        label : str
            Prefix of the cache file generated by hideout.

        Returns
        -------
        object : object
        """
        file_path = generate_path(func, func_args, label)
        logger.info("cache file: {}".format(file_path))
        if env.HIDEOUT_ENABLE_CACHE and self.stage not in env.HIDEOUT_SKIP_STAGES:
            logger.error("trying loading cache")
            if os.path.exists(file_path):
                logger.info("found {}".format(file_path))
                with open(file_path, mode='rb') as f:
                    return pickle.load(f)
            else:
                logger.info("not found cache file...")
        logger.info("generating with func")
        return self._generate_from_function(file_path, func, func_args)

    def _generate_from_function(self, file_path, func, func_args):
        if len(func_args) == 0:
            result = func()
        else:
            result = func(**func_args)
        self._postprocess(result, file_path)
        return result

    def _postprocess(self, result, file_path) -> None:
        if result is not None:
            logger.info("found pickled object ...")
            freeze(result, file_path, self.stage)
        else:
            raise RuntimeError("Any object is loaded ...")
