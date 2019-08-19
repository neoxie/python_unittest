import unittest
import business
import database


class TestBusiness(unittest.TestCase):
    """docstring for TestMain."""
    def test_query_db(self):
        dummy_database = database.MockDatabase()
        result = business.query_db(dummy_database, 'test', 'students')

        self.assertEqual(len(result), 2)
