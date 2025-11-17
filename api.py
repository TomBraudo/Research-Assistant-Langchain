from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents.research import research_with_summary
from utils.logger import get_logger
import json

# Get logger for API
logger = get_logger("api")

# Initialize FastAPI app
app = FastAPI(
    title="Research Agent API",
    description="Web search and summarization agent using Llama 3.3 70B",
    version="1.0.0"
)

# Request/Response models
class ResearchQuery(BaseModel):
    query: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "query": "best machine learning frameworks for beginners"
            }
        }

class ResearchResponse(BaseModel):
    status: str
    data: dict
    
    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "data": {
                    "results": [
                        {
                            "rank": 1,
                            "title": "Example Title",
                            "url": "https://example.com",
                            "summary": "Example summary"
                        }
                    ]
                }
            }
        }

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "service": "Research Agent API",
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {"status": "healthy"}

@app.post("/research", response_model=ResearchResponse)
async def research(query: ResearchQuery):
    """
    Perform web research and return summarized results in JSON format.
    
    Args:
        query: ResearchQuery object containing the search query
        
    Returns:
        ResearchResponse with status and JSON data containing top 5 results
    """
    try:
        logger.info(f"API request received for query: '{query.query}'")
        
        if not query.query.strip():
            logger.warning("Empty query received")
            raise HTTPException(status_code=400, detail="Query cannot be empty")
        
        # Call the research agent
        result_json_str = research_with_summary(query.query)
        
        # Parse the JSON string to validate it
        try:
            result_data = json.loads(result_json_str)
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON returned from research agent: {e}")
            raise HTTPException(
                status_code=500, 
                detail="Failed to parse research results"
            )
        
        logger.info("API request completed successfully")
        
        return ResearchResponse(
            status="success",
            data=result_data
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"API error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

