import os
import app
import unittest


class ThereBeDocsTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_index(self):
        rdata = self.app.get('/')
        assert 'Let there be Docs!' in rdata



if __name__ == '__main__':
    unittest.main()
