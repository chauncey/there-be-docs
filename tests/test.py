import app
import unittest


class ThereBeDocsTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        rsp = self.app.get('/')
        assert 'Let there be Docs!' in rsp.data


if __name__ == '__main__':
    unittest.main()
