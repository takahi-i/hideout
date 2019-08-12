import tempfile
import unittest

import hideout
import hideout.area
from hideout import env
from hideout.file import freeze, _generate_file_path_from_label


def generate():
    return {"foobar": "bar"}


def generate2(baz):
    return {"foobar": baz}


class Generator:
    def generate(self):
        return {"foobar": "bar"}


class Generator2:
    def generate(self, baz):
        return {"foobar": baz}


class TestLoadCache(unittest.TestCase):

    def setUp(self):
        env.HIDEOUT_BASEDIR = tempfile.mkdtemp()
        env.HIDEOUT_ENABLE_CACHE = True

    def test_resume_without_cache(self):
        want_to_load_object = hideout.resume_or_generate(
            label="want-to-load-object", func=generate)
        self.assertEqual({"foobar": "bar"}, want_to_load_object)

    def test_resume_and_save_to_not_exist_dir(self):
        env.HIDEOUT_BASEDIR = tempfile.mkdtemp() + "/foobar"
        want_to_load_object = hideout.resume_or_generate(
            label="want-to-load-object", func=generate)
        self.assertEqual({"foobar": "bar"}, want_to_load_object)

    def test_resume_without_cache_with_param(self):
        want_to_load_object = hideout.resume_or_generate(
            label="want-to-load-object",
            func=generate2,
            func_args={"baz": "uho"})
        self.assertEqual({"foobar": "uho"}, want_to_load_object)

    def test_resume_with_cache(self):
        org_object = {"foobar": "baz"}
        file_path = _generate_file_path_from_label("want-to-load-object")
        freeze(org_object, file_path)
        want_to_load_object = hideout.resume_or_generate(
            label="want-to-load-object",
            func=generate)
        self.assertEqual(org_object, want_to_load_object)

    def test_resume_without_cache_from_instance(self):
        generator = Generator()
        want_to_load_object = hideout.resume_or_generate(
            label="want-to-load-object",
            func=generator.generate)
        self.assertEqual({"foobar": "bar"}, want_to_load_object)

    def test_resume_without_cache_from_instance_with_param(self):
        generator = Generator2()
        want_to_load_object = hideout.resume_or_generate(
            label="want-to-load-object",
            func=generator.generate,
            func_args={"baz": "uho"})
        self.assertEqual({"foobar": "uho"}, want_to_load_object)

    def test_resume_with_disabling_cache(self):
        env.HIDEOUT_ENABLE_CACHE = False  # disabling cache
        org_object = {"foobar": "baz"}
        file_path = _generate_file_path_from_label("want-to-load-object")
        freeze(org_object, file_path)
        want_to_load_object = hideout.resume_or_generate(
            label="want-to-load-object",
            func=generate)
        self.assertEqual({"foobar": "bar"}, want_to_load_object)

    def test_not_resume_disabling_stage(self):
        env.HIDEOUT_SKIP_STAGES = ["preliminary"]
        org_object = {"foobar": "baz"}
        file_path = _generate_file_path_from_label("want-to-load-object")
        freeze(org_object, file_path)
        want_to_load_object = hideout.resume_or_generate(
            label="want-to-load-object",
            func=generate,
            stage="preliminary"
        )
        self.assertEqual({"foobar": "bar"}, want_to_load_object)

    def test_resume_not_disabling_stage(self):
        env.HIDEOUT_SKIP_STAGES = ["preliminary"]
        org_object = {"foobar": "baz"}
        file_path = _generate_file_path_from_label("want-to-load-object")
        freeze(org_object, file_path)
        want_to_load_object = hideout.resume_or_generate(
            label="want-to-load-object",
            func=generate,
            stage="body"
        )
        self.assertEqual({"foobar": "baz"}, want_to_load_object)
