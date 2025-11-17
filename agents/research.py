from langchain_openai import ChatOpenAI
from langchain_core.documents import Document
from utils.config import (
    HUGGINGFACE_API_KEY, 
    HUGGINGFACE_API_BASE, 
    LLAMA_MODEL_NAME, 
    DEFAULT_TEMPERATURE, 
    DEFAULT_MAX_TOKENS,
    validate_config
)
from tools.web_search import web_search
from chains.summary import summarize_documents
from utils.logger import get_logger

# Get logger for this module
logger = get_logger("agents.research")

# Validate configuration
validate_config()
logger.info("✅ Configuration validated successfully")

# Instantiate the Llama 3.3 70B LLM with HuggingFace API
llm = ChatOpenAI(
    model=LLAMA_MODEL_NAME,
    temperature=DEFAULT_TEMPERATURE,
    max_tokens=DEFAULT_MAX_TOKENS,
    base_url=HUGGINGFACE_API_BASE,
    api_key=HUGGINGFACE_API_KEY
)

# Note: Llama 3.3 70B via HuggingFace doesn't support native tool calling
# So we use a simpler approach: always search and then summarize


def research_with_summary(query: str) -> str:
    """
    High-level function to perform web search and summarize the results.
    
    Since Llama 3.3 70B doesn't support native tool calling, we directly
    call the web search and then summarize the results.
    
    Args:
        query: The research query from the user
        
    Returns:
        str: JSON formatted string with top 5 search results and their summaries
    """
    logger.info("=" * 80)
    logger.info(f"🚀 Research process started for query: '{query}'")
    logger.info("=" * 80)
    
    # Step 1: Perform web search
    logger.info("🔍 Calling web search tool...")
    search_results = web_search.invoke(query)
    logger.info(f"✅ Search completed: {len(search_results)} characters retrieved")
    
    # Step 2: Wrap the search results as a LangChain Document for summarization
    logger.info("📦 Preparing documents for summarization...")
    docs = [Document(page_content=search_results)]
    
    # Step 3: Summarize the search results into JSON format with top 5 results
    logger.info("📊 Generating JSON summary...")
    summary = summarize_documents(docs)
    
    logger.info("=" * 80)
    logger.info("🎉 Research process completed successfully!")
    logger.info("=" * 80)
    
    return summary