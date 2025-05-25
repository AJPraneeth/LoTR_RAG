from typing import Any, Union
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import BasePromptTemplate
from langchain_core.retrievers import (
    BaseRetriever,
    RetrieverOutput,
)
from langchain_core.runnables import Runnable
from langchain_core.language_models import LanguageModelLike



def create_stuff_chain(
    llm: LanguageModelLike,
    retriever: Union[BaseRetriever, Runnable[dict[Any, Any], RetrieverOutput]],
    prompt: BasePromptTemplate[Any]
) -> Runnable[Any, Any]:
    """Create a chain that combines a retriever and a language model using a prompt.
    This chain retrieves documents using the retriever, combines them using the
    language model, and formats the output using the provided prompt.

    Args:
        llm (LanguageModelLike): _LanguageModelLike_
        retriever (Union[BaseRetriever, Runnable[dict[Any, Any], RetrieverOutput]]): retriever
            or runnable that returns a retriever output
        prompt (BasePromptTemplate[Any]): prompt template to use for the language model
    and the retrieved documents.

    Returns:
        Runnable[Any, Any]: a runnable that takes a query and returns the
            language model's response to the combined documents.
    """
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    qa_chain = create_retrieval_chain(retriever, combine_docs_chain) # type: ignore
    return qa_chain # type: ignore