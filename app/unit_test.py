import unittest
from cli import CliAction
from api_request import DEFAULT_COMPOUNDS_TO_LOAD


class CliTest(unittest.TestCase):

    def test_cli_action(self):
        self.assertEqual(CliAction.get.value, 'get')
        self.assertEqual(CliAction.load.value, 'load')
        self.assertEqual(CliAction.load_default.value, 'load_default')

    def test_isupper(self):
        self.assertTrue('ADP' in DEFAULT_COMPOUNDS_TO_LOAD)
        self.assertFalse('ATP34' in DEFAULT_COMPOUNDS_TO_LOAD)


if __name__ == '__main__':
    unittest.main()
