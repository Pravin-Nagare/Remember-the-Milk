import unittest
import collection

class TasksTestCase(unittest.TestCase):

    def setUp(self):
        self.app = collection.app.test_client()

if __name__ == '__main__':
    unittest.main()
