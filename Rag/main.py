from Rag.Settings.settings import Settings
from Rag.Emberd.hf_emberding import get_huggingface_embeddings
from Rag.Store.faiss import load_faiss_index
from Rag.Utils.utils import get_config
from Rag.Retriever.faiss import get_all_LORT_source_retrierver
from Rag.LLM.llamafile import connect_llama
from Rag.Prompt.qa import get_base_prompt
from Rag.Chain.stuff import create_stuff_chain

class RAGPipeline:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.qa_chain = self._initialize_pipeline()

    def _initialize_pipeline(self):
        embedding_model = get_huggingface_embeddings(
            model_name=self.settings.HF_MODEL,
            device=self.settings.DEVICE
        )
        vectorstore = load_faiss_index(
            folder_path=self.settings.FAISS_VECTOR_DB_PATH,
            embeddings=embedding_model,
            allow_dangerous_deserialization=True
        )
        retriever = get_all_LORT_source_retrierver(
            vectorstore=vectorstore,
            config=get_config(self.settings.FAISS_CONFIG)
        )
        llm = connect_llama(
            config=get_config(self.settings.LLAMA_FILE_CONFIG),
            base_url=self.settings.LLAMA_FILE_SERVER_URL
        )
        prompt = get_base_prompt()

        if self.settings.RAG_STRATEGY == "stuff":
            return create_stuff_chain(llm=llm, retriever=retriever, prompt=prompt)
        else:
            raise ValueError("Unsupported RAG strategy")

    def run(self, query: str):
        return self.qa_chain.invoke({"input": query, "query": query})
    
    def stream(self,query:str):
        for chunk in self.qa_chain.stream({"input": query, "query": query}):
            if "answer" in chunk:
                yield chunk["answer"]