from langchain.embeddings import HuggingFaceEmbeddings


def get_huggingface_embeddings(model_name: str, device: str):
    """
    Get HuggingFace embeddings model.

    Args:
        model_name (str): Name of the HuggingFace model.
        device (str): Device to use for the model ('cuda' or 'cpu').

    Returns:
        HuggingFaceEmbeddings: HuggingFace embeddings model.
    """
    return HuggingFaceEmbeddings(model_name=model_name,
                                 model_kwargs={'device': device})