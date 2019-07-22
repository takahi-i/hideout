import tempfile
import unittest

import hideout
from hideout import env
from hideout import _generate_file_path
from hideout.utils import freeze


def generate():
    return {"foobar": "bar"}


def generate2(baz):
    return {"foobar": baz}


class Generator:
    def generate(self):
        return {"foobar": "bar"}


class TestLoadCache(unittest.TestCase):

    def setUp(self):
        env.HIDEOUT_BASEDIR = tempfile.mkdtemp()

    def test_resume_without_cache(self):
        want_to_load_object = hideout.Keeper("want-to-load-object").resume(generate)
        self.assertEqual({"foobar": "bar"}, want_to_load_object)

    def test_resume_without_cache_with_param(self):
        want_to_load_object = hideout.Keeper("want-to-load-object").resume(generate2, baz="uho")
        self.assertEqual({"foobar": "uho"}, want_to_load_object)

    def test_resume_with_cache(self):
        org_object = {"foobar": "baz"}
        file_path = _generate_file_path("want-to-load-object")
        freeze(org_object, file_path)
        want_to_load_object = hideout.Keeper("want-to-load-object").resume(generate)
        self.assertEqual(org_object, want_to_load_object) ## NOTE generate with generate()

    def test_resume_without_cache_from_instance(self):
        generator = Generator()
        want_to_load_object = hideout.Keeper("want-to-load-object-3").resume(generator.generate)
        self.assertEqual({"foobar": "bar"}, want_to_load_object)
