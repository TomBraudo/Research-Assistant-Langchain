from langchain_core.tools import tool
import serpapi
from utils.config import SERPAPI_API_KEY
from utils.logger import get_logger

# Get logger for this module
logger = get_logger("tools.web_search")

@tool
def web_search(query: str) -> str:
    """Search the web and return top 10 results with titles, links, and snippets"""
    logger.info(f"🔍 Web search initiated for query: '{query}'")
    try:
        # Use modern serpapi.Client with proper parameters
        client = serpapi.Client(api_key=SERPAPI_API_KEY)
        results = client.search({
            'engine': 'google',
            'q': query
        })
        
        formatted_results = []
        
        # Extract organic results
        organic_results = results.get("organic_results", [])
        
        if organic_results:
            for i, result in enumerate(organic_results[:10], 1):
                title = result.get("title", "No title")
                link = result.get("link", "No link")
                snippet = result.get("snippet", "No snippet available")
                
                formatted_results.append(
                    f"{i}. {title}\n   URL: {link}\n   {snippet}\n"
                )
        
        if formatted_results:
            result_text = "\n".join(formatted_results)
            logger.info(f"✅ Web search completed: Found {len(formatted_results)} results")
            logger.debug(f"Search results: {result_text[:200]}...")  # Log first 200 chars
            return result_text
        else:
            logger.warning("No results found for the query")
            return "No results found for the query."
    except Exception as e:
        logger.error(f"❌ Error performing search: {str(e)}")
        return f"Error performing search: {str(e)}"