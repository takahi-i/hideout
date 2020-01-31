import tempfile
import unittest

import hideout
from hideout import resume
import hideout.area
from hideout import env
from hideout.file import freeze, _generate_file_path_from_label

@resume()
def generate():
    return {"foobar": "bar"}


class TestLoadCache(unittest.TestCase):

    def setUp(self):
        env.HIDEOUT_CACHE_DIR = tempfile.mkdtemp()
        env.HIDEOUT_ENABLE_CACHE = True

    def test_resume_with_cache_decorator(self):
        org_object = {"foobar": "baz"}
        file_path = _generate_file_path_from_label("generate")
        freeze(org_object, file_path)
        want_to_load_object = generate()
        self.assertEqual(org_object, want_to_load_object)
