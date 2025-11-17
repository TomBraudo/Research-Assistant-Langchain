# Research Agent - Docker Deployment

This guide explains how to deploy the Research Agent as a containerized microservice using Docker.

## Prerequisites

- Docker and Docker Compose installed
- API keys for:
  - SerpAPI (for web search)
  - HuggingFace (for Llama 3.3 70B)

## Setup

### 1. Environment Configuration

Create a `.env` file in the `research assistant` directory with your API keys:

```bash
# API Keys (Required)
SERPAPI_API_KEY=your_serpapi_key_here
HUGGINGFACE_API_KEY=your_huggingface_key_here

# HuggingFace Configuration (Optional - defaults provided)
HUGGINGFACE_API_BASE=https://router.huggingface.co/v1
LLAMA_MODEL_NAME=meta-llama/Llama-3.3-70B-Instruct

# LLM Configuration (Optional - defaults provided)
DEFAULT_TEMPERATURE=0.7
DEFAULT_MAX_TOKENS=2048
```

### 2. Build and Run with Docker Compose

```bash
cd "research assistant"
docker-compose up -d
```

This will:
- Build the Docker image
- Start the container
- Expose the API on port 8000
- Mount logs directory for persistence

### 3. Build and Run with Docker (without compose)

```bash
cd "research assistant"

# Build the image
docker build -t research-agent .

# Run the container
docker run -d \
  -p 8000:8000 \
  --env-file .env \
  -v $(pwd)/logs:/app/logs \
  --name research-agent \
  research-agent
```

## API Usage

### Health Check

```bash
curl http://localhost:8000/health
```

### Research Endpoint

**Request:**
```bash
curl -X POST http://localhost:8000/research \
  -H "Content-Type: application/json" \
  -d '{"query": "best Python libraries for data science"}'
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "results": [
      {
        "rank": 1,
        "title": "Top Python Libraries for Data Science",
        "url": "https://example.com",
        "summary": "A comprehensive guide to the most popular..."
      }
    ]
  }
}
```

### Interactive API Documentation

FastAPI provides automatic interactive documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Container Management

### View Logs
```bash
docker-compose logs -f research-agent
```

### Stop the Service
```bash
docker-compose down
```

### Restart the Service
```bash
docker-compose restart
```

### Rebuild After Code Changes
```bash
docker-compose up -d --build
```

## Health Monitoring

The container includes a health check that pings the `/health` endpoint every 30 seconds. You can check the health status:

```bash
docker ps
# Look for "(healthy)" in the STATUS column
```

## Integration with Other Services

Other agents or services can call this API:

```python
import requests

response = requests.post(
    "http://localhost:8000/research",
    json={"query": "your search query here"}
)

if response.status_code == 200:
    data = response.json()
    results = data["data"]["results"]
    print(results)
```

## Troubleshooting

### Container won't start
- Check logs: `docker-compose logs research-agent`
- Verify API keys in `.env` file
- Ensure port 8000 is not in use

### API returns 500 errors
- Check application logs in `./logs/` directory
- Verify API keys are valid
- Check HuggingFace API status

### Network connectivity issues
- Ensure Docker has internet access
- Check firewall settings
- Verify HuggingFace and SerpAPI endpoints are reachable

