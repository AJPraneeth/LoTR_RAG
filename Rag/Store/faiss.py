from langchain_core.embeddings import Embeddings
from langchain.vectorstores import FAISS


def load_faiss_index(folder_path: str, embeddings:Embeddings, allow_dangerous_deserialization: bool = False):
    """
    Load a FAISS index from a local folder.

    Args:
        folder_path (str): Path to the folder containing the FAISS index.
        embeddings: Embeddings model to use for the FAISS index.
        allow_dangerous_deserialization (bool): Whether to allow dangerous deserialization.

    Returns:
        FAISS: Loaded FAISS index.
    """
    return FAISS.load_local(folder_path=folder_path,
                            embeddings=embeddings,
                            allow_dangerous_deserialization=allow_dangerous_deserialization)