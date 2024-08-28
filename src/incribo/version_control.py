import incribo
from sentence_transformers import SentenceTransformer
import numpy as np
import time
import threading
import pytest
import os
import tempfile

def test_version_control_wrapper():
    print("\nTesting VersionControlWrapper")

    # Create initial vector
    initial_vector = np.random.rand(5).astype(np.float32).tolist()

    # Create VersionControlWrapper
    vc = incribo.VersionControlWrapper(initial_vector)

    print(f"Initial vector (version 0): {vc.get_current_vector()}")
    print(f"Version count: {vc.get_version_count()}")

    # Commit new versions
    for i in range(3):
        new_vector = np.random.rand(5).astype(np.float32).tolist()
        version = vc.commit(new_vector)
        print(f"\nCommitted new vector (version {version}): {new_vector}")
        print(f"Current vector: {vc.get_current_vector()}")
        print(f"Version count: {vc.get_version_count()}")

    # Test rollback
    rollback_version = 1
    vc.rollback(rollback_version)
    print(f"\nRolled back to version {rollback_version}")
    print(f"Current vector: {vc.get_current_vector()}")

    # Try invalid rollback
    try:
        vc.rollback(10)
        print("Error: Invalid rollback succeeded")
    except ValueError as e:
        print(f"Caught expected error for invalid rollback: {e}")

    # Final state
    print(f"\nFinal current vector: {vc.get_current_vector()}")
    print(f"Final version count: {vc.get_version_count()}")

    # Verify final state
    assert vc.get_version_count() == 4, f"Expected 4 versions, but got {
        vc.get_version_count()}"
    assert len(vc.get_current_vector()) == 5, f"Expected vector length 5, got {
        len(vc.get_current_vector())}"

    print("\nVersionControlWrapper test completed successfully!")

