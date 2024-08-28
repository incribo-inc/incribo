#test file
import unittest
from incribo import VersionControlWrapper

class TestVersionControl(unittest.TestCase):
    def setUp(self):
        self.vc = VersionControlWrapper([1.0, 2.0, 3.0])

    def test_commit(self):
        new_version = self.vc.commit([4.0, 5.0, 6.0])
        self.assertEqual(new_version, 1)
        self.assertEqual(self.vc.get_current_vector(), [4.0, 5.0, 6.0])

    def test_rollback(self):
        self.vc.commit([4.0, 5.0, 6.0])
        self.vc.rollback(0)
        self.assertEqual(self.vc.get_current_vector(), [1.0, 2.0, 3.0])

    def test_get_version_count(self):
        self.vc.commit([4.0, 5.0, 6.0])
        self.assertEqual(self.vc.get_version_count(), 2)

if __name__ == '__main__':
    unittest.main()
