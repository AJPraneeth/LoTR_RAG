from Rag.Settings.settings import Settings
from Rag.main import RAGPipeline

def main(query: str) -> None:
    """
    Main function to run the RAG pipeline.
    Args:
        query (str): The input query to be processed.
    """
    settings = Settings()
    rag_pipeline = RAGPipeline(settings)
        
    response = rag_pipeline.run(query)
        
    return response
    
if __name__ == "__main__":
    query = "what is Narsil?"
    response = main(query)
    print(response)
        
    
    
    
    
    
    
    
    