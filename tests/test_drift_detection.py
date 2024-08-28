#test file

import unittest
from incribo import DriftManagerWrapper

class TestDriftDetection(unittest.TestCase):
    def setUp(self):
        self.drift_manager = DriftManagerWrapper([1.0, 2.0, 3.0], 0.5)

    def test_check_drift(self):
        self.assertFalse(self.drift_manager.check_drift([1.1, 2.1, 3.1]))
        self.assertTrue(self.drift_manager.check_drift([2.0, 3.0, 4.0]))

    def test_update_threshold(self):
        self.drift_manager.update_threshold(1.0)
        self.assertFalse(self.drift_manager.check_drift([2.0, 3.0, 4.0]))

    def test_get_original_vector(self):
        self.assertEqual(self.drift_manager.get_original_vector(), [1.0, 2.0, 3.0])

if __name__ == '__main__':
    unittest.main()
