import unittest
from  detector_base import TFLiteSingleton
from config import PATH_TO_MODEL

class TestTFLiteSingleton(unittest.TestCase):

    def setUp(self):
        pass

    def test_is_using_edgetpu(self):
        tfs = TFLiteSingleton.get_instance(PATH_TO_MODEL)
        self.assertTrue(tfs.is_using_edgetpu)

if __name__ == '__main__':
    unittest.main()
