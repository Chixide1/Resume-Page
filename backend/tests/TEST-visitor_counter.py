import unittest
import sys
sys.path.append(r"C:\Users\chixi\OneDrive\Desktop\Programming\Azure\Azure-Resume\backend\api\azureResumeCounter")
sys.path.append(r"backend/api/azureResumeCounter")
from counter import updatecount

class TestCounter(unittest.TestCase):

    def test_updatecount(self):
        result = updatecount({'PartitionKey': '0', 'RowKey': '0', 'count': "0"})
        self.assertEqual(result, {'PartitionKey': '0', 'RowKey': '0', 'count': "1"})
## Run the test
if __name__ == '__main__':
    unittest.main(verbosity=2)