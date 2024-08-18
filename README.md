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
Before we get started, it is advised to setup a virtual environment to work in. Next, add your embedding model and generate stateful embeddings with Incribo like so -
```python
from incribo import Embedding

# Create a new embedding and add an associated model for better identification
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
For detailed usage instructions and example use cases, visit our documentation at [docs.incribo.com](https://docs.incribo.com/quickstart).


# 🌐 Contributing
Drop us an email to report a bug, or request a feature here: info@incribo.com


# 🤝 Connect with the founders 1:1 
Connect with us [here](https://cal.com/uma08/30min).


# 💪 Community
Join our growing community around the world, for help, ideas, and everything on AI and beyond:

- Chat with us on [Discord]().
- Follow us on [Twitter](https://twitter.com/IncriboOfficial).
- Connect with us on [LinkedIn](https://www.linkedin.com/company/incribo).



# License
This project is licensed under the Apache 2.0 License - see the [LICENSE](https://github.com/incribo-inc/incribo/blob/main/LICENSE) file for details.
