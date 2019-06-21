# -*- coding: utf-8 -*-
import os

from hideout.keeper import Keeper


def keeper(force=False, skip_list=[], base_dir="./"):
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
    return Keeper(force, skip_list, base_dir)
