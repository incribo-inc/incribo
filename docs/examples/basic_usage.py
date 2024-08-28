from incribo import Embedding, EmbeddingComparator

# Create embeddings
emb1 = Embedding([1.0, 2.0, 3.0], "model1")
emb2 = Embedding([2.0, 3.0, 4.0], "model2")

# Compare embeddings
comparator = EmbeddingComparator()
comparator.add_embedding(emb1)
comparator.add_embedding(emb2)
results = comparator.compare()

print(results)
