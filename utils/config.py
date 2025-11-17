from dotenv import load_dotenv
import os

load_dotenv()

# API Keys
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# API Base URLs - HuggingFace Router endpoint (OpenAI-compatible)
HUGGINGFACE_API_BASE = os.getenv("HUGGINGFACE_API_BASE", "https://router.huggingface.co/v1")

# Model Configuration
LLAMA_MODEL_NAME = os.getenv("LLAMA_MODEL_NAME", "meta-llama/Llama-3.3-70B-Instruct")
DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", "0.7"))
DEFAULT_MAX_TOKENS = int(os.getenv("DEFAULT_MAX_TOKENS", "2048"))

# Validate required API keys
def validate_config():
    """Validate that all required API keys are present"""
    missing_keys = []
    
    if not SERPAPI_API_KEY:
        missing_keys.append("SERPAPI_API_KEY")
    
    if not HUGGINGFACE_API_KEY:
        missing_keys.append("HUGGINGFACE_API_KEY")
    
    if missing_keys:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_keys)}")
    
    return True