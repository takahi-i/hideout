import os
import pickle

from hideout import env


class Keeper:
    def __init__(self, base_dir, force, skip_list=[]):
        self.base_dir = base_dir
        self.force = force
        self.skip_list = skip_list

    def freeze(self, target, file_name, force=True):
        file_path="{}/{}".format(self.base_dir, file_name)
        if (not os.path.exists(file_path)) or force:
            with open(file_path, mode='wb') as f:
                return pickle.dump(target, f)
        return None

    def resume(self, file_name, force=False):
        file_path = "{}/{}".format(self.base_dir, file_name)
        if os.path.exists(file_path) and not force:
            with open(file_path, mode='rb') as f:
                return pickle.load(file_name, f)
        return None
