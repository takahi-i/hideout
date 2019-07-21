import tempfile
import unittest

import hideout
from hideout import env
from hideout.keeper import _generate_file_path
from hideout.utils import freeze


class TestLoadCache(unittest.TestCase):

    def setUp(self):
        env.HIDEOUT_BASEDIR = tempfile.mkdtemp()

    def test_resume_without_cache(self):
        with hideout.resume("want-to-load-object") as want_to_load_object:
            if not want_to_load_object.succeeded_to_load():
                want_to_load_object.set({"foobar": "baz"})
            self.assertEqual({"foobar": "baz"}, want_to_load_object.get())

    def test_resume_with_cache(self):
        org_object = {"foobar": "baz"}
        file_path = _generate_file_path("want-to-load-object")
        freeze(org_object, file_path)
        with hideout.resume("want-to-load-object") as want_to_load_object:
            if not want_to_load_object.succeeded_to_load():
                want_to_load_object.set({"foobar": "bar"})
            self.assertEqual(org_object, want_to_load_object.get())

    def test_resume_without_cache_without_set(self):
        with self.assertRaises(RuntimeError):
            with hideout.resume("no-such-object") as want_to_load_object:
                self.assertEqual(want_to_load_object.get(), None)
