import os
import json
import unittest
from pathlib import Path
from streaming_manager import manager

class ManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.tmpfile = Path('test_accounts.json')
        if self.tmpfile.exists():
            self.tmpfile.unlink()

    def tearDown(self):
        if self.tmpfile.exists():
            self.tmpfile.unlink()

    def test_add_and_list(self):
        manager.add_account(self.tmpfile, {'username': 'user1', 'service': 'netflix', 'plan': 'basic'})
        accounts = manager.list_accounts(self.tmpfile)
        self.assertEqual(len(accounts), 1)
        self.assertEqual(accounts[0]['username'], 'user1')

    def test_remove(self):
        manager.add_account(self.tmpfile, {'username': 'user1', 'service': 'netflix', 'plan': 'basic'})
        manager.remove_account(self.tmpfile, 'user1')
        accounts = manager.list_accounts(self.tmpfile)
        self.assertEqual(len(accounts), 0)

if __name__ == '__main__':
    unittest.main()
