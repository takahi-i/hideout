import os


HIDEOUT_WITHOUT_CACHE = bool(os.getenv('HIDEOUT_WITHOUT_CACHE', False))
HIDEOUT_BASEDIR = os.getenv('HIDEOUT_BASEDIR', './')
HIDEOUT_SKIP_STAGES = os.getenv('HIDEOUT_BASEDIR', '').split(",")
