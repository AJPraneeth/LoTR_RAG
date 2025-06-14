from pydantic_settings import BaseSettings,SettingsConfigDict


# combine env and configs
# https://medium.com/@jayanthsarma8/config-management-with-pydantic-base-settings-de22b79fd191

class Settings(BaseSettings):
    HF_MODEL : str 
    FAISS_VECTOR_DB_PATH : str
    RAG_STRATEGY : str
    LLAMA_FILE_SERVER_URL : str
    DEVICE : str
    FAISS_CONFIG : str
    LLAMA_FILE_CONFIG : str
    
    model_config =SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        case_sensitive= True
    )