# Research Agent - Quick Start Guide

Get the Research Agent API running in Docker in 3 simple steps.

## Step 1: Create Environment File

Create a `.env` file with your API keys:

```bash
SERPAPI_API_KEY=your_serpapi_key_here
HUGGINGFACE_API_KEY=your_huggingface_key_here
```

## Step 2: Start the Service

```bash
docker-compose up -d
```

The API will be available at: http://localhost:8000

## Step 3: Test It

**Option A: Web Browser**
- Visit http://localhost:8000/docs for interactive API documentation

**Option B: Command Line**
```bash
# Test with curl
curl -X POST http://localhost:8000/research \
  -H "Content-Type: application/json" \
  -d '{"query": "best Python web frameworks"}'
```

**Option C: Test Script**
```bash
python test_api.py "your search query here"
```

## Example Response

```json
{
  "status": "success",
  "data": {
    "results": [
      {
        "rank": 1,
        "title": "Top 10 Python Web Frameworks in 2024",
        "url": "https://example.com/frameworks",
        "summary": "Django and Flask lead the pack..."
      }
    ]
  }
}
```

## Stopping the Service

```bash
docker-compose down
```

## Troubleshooting

**Container not starting?**
- Check logs: `docker-compose logs -f`
- Verify `.env` file exists with valid API keys

**API returning errors?**
- Check logs in `./logs/` directory
- Verify API keys are active

For detailed documentation, see [README.Docker.md](./README.Docker.md)

