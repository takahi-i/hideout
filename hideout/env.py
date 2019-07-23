import os
import distutils.util

HIDEOUT_BASEDIR = os.getenv('HIDEOUT_BASEDIR', './')
HIDEOUT_SKIP_STAGES = os.getenv('HIDEOUT_BASEDIR', '').split(",")
HIDEOUT_SUPPRESS_CACHE = bool(distutils.util.strtobool(os.getenv('HIDEOUT_SUPPRESS_CACHE', "False")))  # see https://qiita.com/koemu/items/fd333fd8ed14f31fbca6
