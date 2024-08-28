# Developer docs: https://docs.incribo.com/quickstart

import incribo
from sentence_transformers import SentenceTransformer
import numpy as np
import time
import threading
import pytest
import os
import tempfile

def test_history_tracker_wrapper(
    comparison_results,
    best_model,
    dynamic_emb_initial,
    dynamic_emb_updated
):
    print("\nTesting HistoryTrackerWrapper")
    max_history = 10
    tracker = incribo.HistoryTrackerWrapper(max_history)

    # Add record for cosine similarity from EmbeddingComparator test
    timestamp = time.time()
    cosine_similarity = comparison_results.get(
        'all-MiniLM-L6-v2 vs paraphrase-MiniLM-L3-v2')
    if cosine_similarity:
        tracker.add_record(timestamp, cosine_similarity)
        print(f"Added record for cosine similarity: ({
              timestamp}, {cosine_similarity})")

    # Add records for L2 norms
    for model in ['all-MiniLM-L6-v2', 'paraphrase-MiniLM-L3-v2']:
        l2_norm = comparison_results.get(f'{model} L2 Norm')
        if l2_norm:
            timestamp += 1
            tracker.add_record(timestamp, l2_norm)
            print(f"Added record for {
                  model} L2 Norm: ({timestamp}, {l2_norm})")

    # Add records from DynamicEmbeddingWrapper test
    for i, vector in enumerate([dynamic_emb_initial, dynamic_emb_updated]):
        timestamp += 1
        average_value = sum(vector) / len(vector)
        tracker.add_record(timestamp, average_value)
        print(f"Added record for DynamicEmbedding {
            'initial' if i == 0 else 'updated'}: ({timestamp},{average_value})"
        )

    # Get the history
    history = tracker.get_history()
    print("\nFinal history:")
    for record in history:
        print(record)

    assert len(history) <= max_history, f"Expected at most {
        max_history} records, but got {len(history)}"

    print("\nHistoryTrackerWrapper test passed successfully!")

