from typing import Dict, Any, Union
from omegaconf import DictConfig
from langchain.vectorstores import FAISS


def get_all_LORT_source_retrierver(vectorstore: FAISS, config: Union[DictConfig, Dict[str, Any]]):
    """
    Get a retriever for the LORT source.

    Args:
        vectorstore (FAISS): FAISS vector store.
        config (DictConfig or dict): Configuration dictionary.

    Returns:
        FAISS: FAISS retriever.
    """
    if config["retriever"]["search_type"] == "mmr":
        retriever = vectorstore.as_retriever(
            search_type=config["retriever"]["search_type"],
            search_kwargs={
                "k": config["retriever"]["k"],
                "fetch_k": config["retriever"]["fetch_k"],
                "lambda_mult": config["retriever"]["lambda_mult"],
            },
        )
    elif config["retriever"]["search_type"] == "similarity_score_threshold":
        retriever = vectorstore.as_retriever(
            search_type=config["retriever"]["search_type"],
            search_kwargs={"score_threshold": config["retriever"]["score_threshold"]},
        )
    else:  # Covers both 'similarity' and fallback
        retriever = vectorstore.as_retriever(
            search_kwargs={"k": config["retriever"]["k"]}
        )

    return retriever
