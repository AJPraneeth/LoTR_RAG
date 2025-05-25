from langchain_community.llms.llamafile import Llamafile
from typing import Any


def connect_llama(config: dict[str, Any],base_url:str) -> Llamafile:
    """
    Connect to the LlamaFile model with the given configuration.
    
    Args:
        config (dict[str, Any]): Llama configuration parameters
        base_url (str): local or remote URL to the Llama model
        (e.g. http://localhost:8000 or http://

    Returns:
        Llamafile: Llamafile model instance
    """

    
    # Initialize the LlamaFile model
    llm = Llamafile(base_url=base_url,
                    streaming=config["streaming"],
                    temperature=config["temperature"],
                    top_k=config["top_k"],
                    top_p=config["top_p"],
                    min_p=config["min_p"],
                    n_predict=config["n_predict"],
                    n_keep=config["n_keep"],
                    tfs_z=config["tfs_z"],
                    typical_p=config["typical_p"],
                    repeat_penalty=config["repeat_penalty"],
                    repeat_last_n=config["repeat_last_n"],
                    penalize_nl=config["penalize_nl"],
                    presence_penalty=config["presence_penalty"],
                    frequency_penalty=config["frequency_penalty"],
                    mirostat=config["mirostat"],
                    mirostat_tau=config["mirostat_tau"],
                    mirostat_eta=config["mirostat_eta"])
    
    # Return the initialized model
    return llm