from unittest import TestCase

import gnodatapackages.gno_gen_stopwords as gno

class TestJoke(TestCase):
    def test_is_string(self):
        s = gno.test()
        self.assertTrue(isinstance(s, str))