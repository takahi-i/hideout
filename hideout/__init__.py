# -*- coding: utf-8 -*-
from hideout.keeper import Keeper


def keeper(force=False, skip_list=[], base_dir="./"):
    return Keeper(force, skip_list, base_dir)
