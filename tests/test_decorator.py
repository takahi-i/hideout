import tempfile
import unittest

import hideout
from hideout import resumable
import hideout.area
from hideout import env
from hideout.file import freeze, _generate_file_path_from_label

@resumable()
def generate():
    return {"foobar": "bar"}


class Generator:
    @resumable(label="generate")
    def generate(self):
        return {"foobar": "bar"}


class Generator2:
    @resumable()
    def generate(self, baz):
        return {"foobar": baz}


class TestLoadCache(unittest.TestCase):

    def setUp(self):
        env.HIDEOUT_CACHE_DIR = tempfile.mkdtemp()
        env.HIDEOUT_ENABLE_CACHE = True

    def test_resume_without_cache(self):
        want_to_load_object = generate()
        self.assertEqual({"foobar": "bar"}, want_to_load_object)

    def test_resume_with_cache_decorator(self):
        org_object = {"foobar": "baz"}
        file_path = _generate_file_path_from_label("generate")
        freeze(org_object, file_path)
        want_to_load_object = generate()
        self.assertEqual(org_object, want_to_load_object)

    def test_resume_without_cache_from_instance(self):
        generator = Generator()
        want_to_load_object = generator.generate()
        self.assertEqual({"foobar": "bar"}, want_to_load_object)

    def test_resume_with_cache_method_decorator(self):
        org_object = {"foobar": "baz"}
        file_path = _generate_file_path_from_label("generate")
        freeze(org_object, file_path)
        generator = Generator()
        want_to_load_object = generator.generate()
        self.assertEqual(org_object, want_to_load_object)

    def test_resume_without_cache_from_instance_with_param(self):
        generator = Generator2()
        want_to_load_object = generator.generate(baz="uho")
        self.assertEqual({'foobar': 'uho'}, want_to_load_object)