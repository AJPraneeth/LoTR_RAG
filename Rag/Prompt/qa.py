from langchain.prompts import ChatPromptTemplate

def get_base_prompt() -> ChatPromptTemplate:
    """
    Get the prompt template for the question-answering task.

    Returns:
        ChatPromptTemplate: The prompt template for the task.
    """
    # Define the prompt template
    prompt = ChatPromptTemplate.from_messages([ # type: ignore
        ("system", "You are a Tolkien scholar assistant."),
        ("system", "Use the provided LOTR context to answer the question with citations."),
        ("human", "Context: {context}\n\nQuestion: {query}\nAnswer:")
    ])

    return prompt
