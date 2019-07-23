import os


HIDEOUT_BASEDIR = os.getenv('HIDEOUT_BASEDIR', './')
HIDEOUT_SKIP_STAGES = os.getenv('HIDEOUT_BASEDIR', '').split(",")
HIDEOUT_SUPPRESS_CACHE = bool(os.getenv('HIDEOUT_SUPPRESS_CACHE', False))
