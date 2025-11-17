from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from utils.config import (
    HUGGINGFACE_API_KEY, 
    HUGGINGFACE_API_BASE, 
    LLAMA_MODEL_NAME, 
    DEFAULT_TEMPERATURE, 
    DEFAULT_MAX_TOKENS
)
from utils.logger import get_logger

# Get logger for this module
logger = get_logger("chains.summary")

# Instantiate LLM with Llama 3.3 70B via HuggingFace
llm = ChatOpenAI(
    model=LLAMA_MODEL_NAME,
    temperature=DEFAULT_TEMPERATURE,
    max_tokens=DEFAULT_MAX_TOKENS,
    base_url=HUGGINGFACE_API_BASE,
    api_key=HUGGINGFACE_API_KEY
)

# Create a modern chat prompt template for summarization in JSON format
summary_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful assistant that summarizes search results into JSON format.
You must return ONLY valid JSON (no markdown, no extra text) in the following structure:
{{
  "results": [
    {{
      "rank": 1,
      "title": "...",
      "url": "...",
      "summary": "..."
    }}
  ]
}}

Extract the top 5 search results from the provided content and create a concise summary for each.
Return ONLY the JSON object, nothing else."""),
    ("user", "Extract and summarize the top 5 search results from the following content into JSON format:\n\n{text}")
])

# Create a chain using the modern LCEL (LangChain Expression Language) syntax
summary_chain = summary_prompt | llm

def summarize_documents(docs):
    """
    Accepts docs - a list of LangChain Document objects or dicts with 'page_content'.
    Uses modern LangChain v1.0 direct invocation to summarize the content into JSON format.
    
    Args:
        docs: List of Document objects with 'page_content' attribute
        
    Returns:
        str: JSON formatted string containing top 5 search results with summaries
    """
    logger.info(f"📝 Summarization initiated for {len(docs)} document(s)")
    
    # Combine all document content into a single text
    combined_text = "\n\n".join([doc.page_content for doc in docs])
    logger.debug(f"Combined text length: {len(combined_text)} characters")
    
    # Invoke the chain with the combined text
    logger.info("🤖 Calling Llama 3.3 70B for JSON summarization...")
    response = summary_chain.invoke({"text": combined_text})
    
    # Extract the content from the response
    summary = response.content
    logger.info(f"✅ JSON summarization completed: {len(summary)} characters")
    logger.debug(f"Summary preview: {summary[:150]}...")
    
    return summary

# Example usage: pass a list of search result docs to summarize_documents
# docs = [Document(page_content=result_text) for result_text in web_search_results_texts]
# json_summary = summarize_documents(docs)
# print(json_summary)  # Returns JSON formatted string
