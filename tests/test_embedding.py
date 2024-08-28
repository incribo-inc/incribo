#test file
import unittest
from incribo import Embedding, EmbeddingComparator

class TestEmbedding(unittest.TestCase):
    def setUp(self):
        self.embedding = Embedding([1.0, 2.0, 3.0], "test_model")

    def test_get_vector(self):
        self.assertEqual(self.embedding.get_vector(), [1.0, 2.0, 3.0])

    def test_get_model(self):
        self.assertEqual(self.embedding.get_model(), "test_model")

class TestEmbeddingComparator(unittest.TestCase):
    def setUp(self):
        self.comparator = EmbeddingComparator()
        self.comparator.add_embedding(Embedding([1.0, 0.0], "model1"))
        self.comparator.add_embedding(Embedding([0.0, 1.0], "model2"))

    def test_compare(self):
        results = self.comparator.compare()
        self.assertIn("model1 vs model2", results)
        self.assertLess(results["model1 vs model2"], 1.0)

    def test_get_best_model(self):
        best_model = self.comparator.get_best_model()
        self.assertIn(best_model, ["model1", "model2"])

if __name__ == '__main__':
    unittest.main()
