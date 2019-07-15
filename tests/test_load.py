import pickle
import tempfile
import unittest

import hideout

from hideout import Keeper, env


def freeze(file_path, target_object):
    with open(file_path, mode='wb') as f:
        return pickle.dump(target_object, f)

class TestLoadCache(unittest.TestCase):

    def setUp(self):
        env.HIDEOUT_BASEDIR = tempfile.mkdtemp()

    def test_resume_without_cache(self):
        with hideout.resume(file_prefix="want-to-load-object") as want_to_load_object:
            if not want_to_load_object.succeeded_to_load():
                want_to_load_object.set({"foobar": "baz"})
            self.assertEqual({"foobar": "baz"}, want_to_load_object.get())

    def test_resume_with_cache(self):
        org_object = {"foobar": "baz"}
        freeze(env.HIDEOUT_BASEDIR + "/want-to-load-object.pickle" , org_object)
        with hideout.resume(file_prefix="want-to-load-object") as want_to_load_object:
            if not want_to_load_object.succeeded_to_load():
                want_to_load_object.set({"foobar": "bar"})
            self.assertEqual(org_object, want_to_load_object.get())
