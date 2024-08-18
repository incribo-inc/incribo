# incribo
Incribo lets you add **state** to your embeddings. Using it, you can track how embeddings change over time, compare different embeddings to see their similarities and stream new data to update embeddings on the fly. 

- **Real-time Embedding Updates**: Efficient handling of evolving, dynamic data.
- **Compare embedding qualities**: Compare different embeddings and evaluate their quality using customizable metrics.
- **Versioning & Control**: Create multiple versions of embeddings and track them over time with rollback abilities.
- **Streaming data**: Stream data from multiple sources.
- **Cross-Platform Compatibility**: Hassle-free hosted solution.


# 🔧 Quick install
```python
#Download the Python package
pip install incribo
```

# ✨ Basic Usage
Before we get started, it is advised to setup a virtual environment to work in. Incribo works with all embedding models -
```python
from incribo import Embedding

# Create a new embedding
emb = Embedding([1.0, 2.0, 3.0], "bert-base-uncased")

# Get the vector
vector = emb.get_vector()
print(f"Embedding vector: {vector}")

# Get the model name
model = emb.get_model()
print(f"Model: {model}")

# print the Embedding object 
print(emb)
```

# 📖 Documentation

# 🔗 Be a part of our Community

# 🤝 Connect with the founders 1:1 

# 🌐 Contributing

# Anonymous Telemetry

# Citations
