# Developer docs: https://docs.incribo.com/quickstart

import incribo
from sentence_transformers import SentenceTransformer
import numpy as np
import time
import threading
import pytest
import os
import tempfile


def test_consistency_manager_wrapper():
    print("\nTesting ConsistencyManagerWrapper")

    # Create initial vector
    initial_vector = np.random.rand(5).tolist()

    # Create ConsistencyManagerWrapper
    consistency_manager = incribo.ConsistencyManagerWrapper(initial_vector)

    print(f"Initial vector: {consistency_manager.get_vector()}")
    print(f"Initial version: {consistency_manager.get_version()}")

    # Function to update the vector
    def update_vector():
        new_vector = np.random.rand(5).tolist()
        new_version = consistency_manager.update(new_vector)
        print(f"Updated to version {new_version}: {new_vector}")

    # Function to read the vector
    def read_vector():
        vector = consistency_manager.get_vector()
        version = consistency_manager.get_version()
        print(f"Read version {version}: {vector}")

    # Create threads for concurrent updates and reads
    threads = []
    for _ in range(5):
        threads.append(threading.Thread(target=update_vector))
        threads.append(threading.Thread(target=read_vector))

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Final state
    final_vector = consistency_manager.get_vector()
    final_version = consistency_manager.get_version()
    print(f"\nFinal vector: {final_vector}")
    print(f"Final version: {final_version}")

    # Verify final state
    assert final_version == 5, f"Expected 5 updates, but got {final_version}"
    assert len(final_vector) == 5, f"Expected vector length 5, but got {
        len(final_vector)}"

    print("\nConsistencyManagerWrapper test completed successfully!")

