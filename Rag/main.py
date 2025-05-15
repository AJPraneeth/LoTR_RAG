from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain_community.llms.llamafile import Llamafile
from langchain.prompts import PromptTemplate,ChatPromptTemplate
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
import torch


device = 'cuda' if torch.cuda.is_available() else 'cpu'


embedding_model=HuggingFaceEmbeddings(model_name='sentence-transformers/all-mpnet-base-v2',
                                      model_kwargs = {'device': device})

vectorstore = FAISS.load_local(folder_path="vector_db/faiss_index_hybride_all_books",
                               embeddings=embedding_model,
                               allow_dangerous_deserialization=True)


retriever = vectorstore.as_retriever(search_kwargs={"k": 10}) 


llm = Llamafile()


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Tolkien scholar assistant."),
    ("system", "Use the provided LOTR context to answer the question with citations."),
    ("human", "Context: {context}\n\nQuestion: {query}\nAnswer:")
])


combine_docs_chain = create_stuff_documents_chain(llm, prompt)
qa_chain = create_retrieval_chain(retriever, combine_docs_chain)


query = 'what is Narsil?'


response = qa_chain.invoke({"input": query, "query": query})


for chunk in qa_chain.stream({"input": query, "query": query}):
    if "answer" in chunk:
        print(chunk["answer"], end="", flush=True)

print()