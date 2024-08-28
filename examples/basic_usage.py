from incribo import Embedding, EmbeddingStreamer

# Basic embedding creation and manipulation
embedding = Embedding([1.0, 2.0, 3.0], "example_model")
print(f"Embedding vector: {embedding.get_vector()}")
print(f"Embedding model: {embedding.get_model()}")

# Simple streaming example
def simple_embedding_function(text):
    return [len(text)]  # Oversimplified for demonstration

streamer = EmbeddingStreamer(simple_embedding_function)
streamer.update_embedding("example_key", "This is a test", 0.5)
result = streamer.get_embedding("example_key")
print(f"Streamed embedding: {result}")
