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


def generate_path(func, func_args, label=None):
    """
    Return file path from arguments. If label is specified, this function returns the
    file name with the specified label. Otherwise this function returns the file path
    from specified function name and the function arguments.

    Parameters
    ----------
    func
        function to generate object
    func_args
        arguments for the specified function
    label
        file prefix

    Returns
    -------
    str : file path
    """
    if label:
        file_path = _generate_file_path_from_label(label)
    else:
        file_path = _generate_file_path_from_func(func, func_args)
    return file_path


def _generate_file_path_from_label(label):
    return os.path.join(env.HIDEOUT_BASEDIR, "{}.pickle".format(label))


def _generate_file_path_from_func(func, func_args={}):
    class_name = _get_class_that_defined_method(func)
    label = "{}".format(class_name)
    for arg_name in func_args:
        arg_value = str(func_args[arg_name])
        if len(arg_value) > 10:
            arg_value = hashlib.md5(arg_value.encode("utf-8")).hexdigest()[0:10]
        label += "-{}-{}".format(arg_name, arg_value)
    return _generate_file_path_from_label(label)


def _get_class_that_defined_method(method):
    class_name = ""
    names = method.__qualname__.split('.')
    for i, attr in enumerate(names):
        class_name += "{}".format(attr)
        if i != len(names) - 1:
            class_name += "-"
    return class_name
