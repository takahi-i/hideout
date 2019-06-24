# -*- coding: utf-8 -*-
import os
import pickle
import contextlib
from hideout import env


@contextlib.contextmanager
def resume(file_name):
    file_path = "{}/{}".format(env.HIDEOUT_BASEDIR, file_name)
    if os.path.exists(file_path) and not env.HIDEOUT_FORCE_CACHE:
        with open(file_path, mode='rb') as f:
            yield pickle.load(f)
    else:
        yield None


@contextlib.contextmanager
def freeze(target, file_name):
    file_path="{}/{}".format(env.HIDEOUT_BASEDIR, file_name)
    if (not os.path.exists(file_path)) or env.HIDEOUT_FORCE_CACHE:
        with open(file_path, mode='wb') as f:
            return pickle.dump(target, f)
