import hashlib
import os
import pickle

from hideout import env
from hideout.log import logger


def freeze(target_object: object, file_path: str, stage: str=None) -> None:
    """
    Save the given object int the specified file path. When HIDEOUT_ENABLE_CACHE
    is set to False or HIDEOUT_SKIP_STAGE contains given stage name, the object is
    not save in to the cache file.

    Parameters
    ----------
    target_object : object
        The object is save into the given file path.
    file_path
        Path to save given object.
    stage
        Stage name in the program.
    Returns
    -------
    """
    if not env.HIDEOUT_ENABLE_CACHE or stage in env.HIDEOUT_SKIP_STAGES:
        logger.info("skip saving to cache file ...")
        return

    if not os.path.exists(env.HIDEOUT_BASEDIR):
        os.makedirs(env.HIDEOUT_BASEDIR, exist_ok=True)

    logger.info("saving {}".format(file_path))
    with open(file_path, mode='wb') as f:
        return pickle.dump(target_object, f)


def _generate_file_path_from_label(label):
    return "{}/{}.pickle".format(env.HIDEOUT_BASEDIR, label)


def _generate_file_path_from_func(func, func_args={}):
    label = func.__name__
    for arg_name in func_args:
        arg_value = str(func_args[arg_name])
        if len(arg_value) > 10:
            arg_value = hashlib.md5(arg_value.encode("utf-8")).hexdigest()[0:10]
        label += "-{}-{}".format(arg_name, arg_value)
    return _generate_file_path_from_label(label)


def generate_file_path(func, func_args, label=None):
    if label is not None:
        file_path = _generate_file_path_from_label(label)
    else:
        file_path = _generate_file_path_from_func(func, func_args)
    return file_path
