import os


HIDEOUT_FORCE_CACHE = bool(os.getenv('HIDEOUT_FORCE_CACHE', False))
HIDEOUT_BASEDIR = os.getenv('HIDEOUT_BASEDIR', './')
HIDEOUT_SKIP_STAGES = os.getenv('HIDEOUT_BASEDIR', '').split(",")
