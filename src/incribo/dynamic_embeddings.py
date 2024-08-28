import incribo
from sentence_transformers import SentenceTransformer
import numpy as np
import time
import threading
import pytest
import os
import tempfile


def test_dynamic_embedding_wrapper():
    print("\nTesting DynamicEmbeddingWrapper")

    # Create an initial vector
    initial_vector = np.random.rand(10).tolist()

    print("Creating DynamicEmbeddingWrapper with initial vector")
    dynamic_emb = incribo.DynamicEmbeddingWrapper(initial_vector)

    print("Initial vector:")
    print(dynamic_emb.get_vector())

    # Create a new vector to update
    new_vector = np.random.rand(10).tolist()

    print("\nUpdating with new vector")
    dynamic_emb.update(new_vector)

    print("Updated vector:")
    print(dynamic_emb.get_vector())

    # Verify that the update worked correctly
    assert dynamic_emb.get_vector() == new_vector, (
        "Update failed: vectors do not match"
    )

    print("\nDynamicEmbeddingWrapper test passed successfully!")
    return initial_vector, new_vector
