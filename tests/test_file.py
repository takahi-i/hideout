import os
import unittest

from hideout.file import generate_path


def generate(baz):
    return {"foobar": baz}


class TestFile(unittest.TestCase):

    def test_generate_file_name_with_label(self):
        self.assertTrue("large_object.pickle",
                        os.path.basename(generate_path(
                            func=generate,
                            func_args={"baz": [0, 1, 2, 3, 4, 5, 7, 6, 8, 9, 10]},
                            label="large_object"
                        )))

    def test_generate_file_name_from_hash(self):
        self.assertTrue("generate2-baz-6979983cbc.pickle",
                        os.path.basename(generate_path(
                            func=generate,
                            func_args={"baz": [0, 1, 2, 3, 4, 5, 7, 6, 8, 9, 10]})))
