import incribo
from sentence_transformers import SentenceTransformer
import numpy as np
import time
import threading
import pytest
import os
import tempfile

def test_branch_manager_wrapper():
    print("\nTesting BranchManagerWrapper")

    # Create initial vector
    initial_vector = np.random.rand(5).astype(np.float32).tolist()

    # Create BranchManagerWrapper
    bm = incribo.BranchManagerWrapper(initial_vector)

    print(f"Initial vector (branch 0): {bm.get_active_vector()}")
    print(f"Branch count: {bm.get_branch_count()}")

    # Create new branches
    for i in range(2):
        new_vector = np.random.rand(5).astype(np.float32).tolist()
        new_branch = bm.create_branch(new_vector)
        print(f"\nCreated new branch {new_branch}: {new_vector}")
        print(f"Active vector: {bm.get_active_vector()}")
        print(f"Branch count: {bm.get_branch_count()}")

    # Switch to first branch
    bm.switch_branch(0)
    print(f"\nSwitched to branch 0")  # noqa: F541
    print(f"Active vector: {bm.get_active_vector()}")

    # Merge branches
    bm.merge_branches(0, 1)
    print(f"\nMerged branches 0 and 1")  # noqa: F541
    print(f"Active vector (merged): {bm.get_active_vector()}")
    print(f"Branch count: {bm.get_branch_count()}")

    # Try invalid branch switch
    try:
        bm.switch_branch(10)
        print("Error: Invalid branch switch succeeded")
    except ValueError as e:
        print(f"Caught expected error for invalid branch switch: {e}")

    # Try invalid branch merge
    try:
        bm.merge_branches(0, 10)
        print("Error: Invalid branch merge succeeded")
    except ValueError as e:
        print(f"Caught expected error for invalid branch merge: {e}")

    # Final state
    print(f"\nFinal active vector: {bm.get_active_vector()}")
    print(f"Final branch count: {bm.get_branch_count()}")

    # Verify final state
    assert bm.get_branch_count() == 4, f"Expected 4 branches, but got {
        bm.get_branch_count()}"
    assert len(bm.get_active_vector()) == 5, f"Expected vector length 5, got {
        len(bm.get_active_vector())}"

    print("\nBranchManagerWrapper test completed successfully!")
