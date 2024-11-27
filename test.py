import unittest
from InMemoryDB import InMemoryDB

class TestInMemoryDB(unittest.TestCase):
    def setUp(self):
        #initialize new InMemoryDB instance before each test
        self.db = InMemoryDB()

    def test_get_without_transaction(self):
        #ensure returns None when the key does not exist and no transaction is in progress
        self.assertIsNone(self.db.get("A"))

    def test_put_without_transaction(self):
        #ensure an exception is raised when no transaction is in progress
        with self.assertRaises(Exception):
            self.db.put("A", 5)

    def test_transaction_flow(self):
        #begin new transaction
        self.db.begin_transaction()
        #put a new key-value pair within the transaction
        self.db.put("A", 5)
        #ensure that get(key) does not see uncommitted changes
        self.assertIsNone(self.db.get("A"))
        #update the value of the existing key within the transaction
        self.db.put("A", 6)
        #commit the transaction to apply changes
        self.db.commit()
        #get should return the updated value
        self.assertEqual(self.db.get("A"), 6)

    def test_rollback(self):
        #begin new transaction
        self.db.begin_transaction()
        #put a new key-value pair within the transaction
        self.db.put("B", 10)
        #ensure that get(key) does not see uncommitted changes
        self.assertIsNone(self.db.get("B"))
        #rollback the transaction to discard changes
        self.db.rollback()
        #get should return None as changes were not committed
        self.assertIsNone(self.db.get("B"))

    def test_commit_without_transaction(self):
        #ensure an exception is raised when no transaction is in progress
        with self.assertRaises(Exception):
            self.db.commit()

    def test_rollback_without_transaction(self):
        #ensure an exception is raised when no transaction is in progress
        with self.assertRaises(Exception):
            self.db.rollback()

    def test_nested_transaction_error(self):
        #begin new transaction
        self.db.begin_transaction()
        #ensure that starting another transaction while one is in progress raises an exception
        with self.assertRaises(Exception):
            self.db.begin_transaction()

if __name__ == "__main__":
    unittest.main()
