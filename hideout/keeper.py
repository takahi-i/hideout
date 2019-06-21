import os
import pickle

from hideout import env


class Keeper:
    def __init__(self, force=False, skip_list=[], base_dir="./"):
        self.base_dir = base_dir
        self.skip_list = skip_list
        self.force = force or env.HIDEOUT_FORCE_CACHE

    def freeze(self, target, file_name, force):
        if os.path.exists(file_name) and not force:
            with open("{}/{}".format(env.HIDEOUT_BASEDIR, file_name), mode='wb') as f:
                return pickle.dump(target, f)

    def resume(self, file_name, force):
        if os.path.exists(file_name) and not force:
            with open("{}/{}".format(env.HIDEOUT_BASEDIR, file_name), mode='rb') as f:
                return pickle.load(file_name, f)
