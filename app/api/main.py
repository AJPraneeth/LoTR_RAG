from fastapi import FastAPI
from contextlib import asynccontextmanager
from Rag.main import RAGPipeline
from Rag.Settings.settings import Settings
from fastapi.responses import StreamingResponse

rag_pipeline: RAGPipeline = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global rag_pipeline
    settings = Settings()
    rag_pipeline = RAGPipeline(settings=settings)
    
    print("🚀 RAGPipeline initialized.")
    try:
        yield
    finally:
        # 👇 CLEAN-UP LOGIC STARTS HERE
        if rag_pipeline:
            if hasattr(rag_pipeline, "close") and callable(rag_pipeline.close):
                rag_pipeline.close()  # e.g., close DB connections, release memory
                print("🧹 RAGPipeline resources cleaned up.")
            else:
                print("⚠️ No 'close()' method found on RAGPipeline.")
        else:
            print("⚠️ RAGPipeline was not initialized.")
        # 👇 Optionally force garbage collection or clear cache
        import gc
        gc.collect()
        print("✅ Cleanup complete.")

app = FastAPI(lifespan=lifespan)




@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/ask_qa")
def ask_qa(query:str):
    """
    Endpoint to ask a question and get an answer.
    """
    global rag_pipeline
    if not rag_pipeline:
        return {"error": "RAGPipeline is not initialized."}
    
    try:
        def generate():
            for chunk in rag_pipeline.stream(query):
                yield chunk
        
        return StreamingResponse(generate(), media_type="text/plain")

    except Exception as e:
        return {"error": str(e)}