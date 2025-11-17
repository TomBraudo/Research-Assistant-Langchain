# Research Assistant

An intelligent web research agent that searches the web and provides AI-powered summarized results in structured JSON format.

## 🎯 What It Does

The Research Assistant:
1. **Searches** the web using SerpAPI (top 10 Google results)
2. **Analyzes** search results using Llama 3.3 70B AI model
3. **Summarizes** findings into structured JSON format
4. **Returns** the top 5 most relevant results with concise summaries

## 🏗️ Architecture

```
User → Research Agent API → SerpAPI (Web Search)
              ↓
        Llama 3.3 70B (via HuggingFace)
              ↓
        JSON Summary Output
```

**Features:**
- RESTful API with FastAPI
- Asynchronous request handling
- Comprehensive logging system
- Docker-ready deployment
- Interactive API documentation (Swagger UI)
- Health check endpoints

## 🚀 Quick Start

See [QUICKSTART.md](./QUICKSTART.md) for the fastest way to get started.

### Option 1: Docker (Recommended)

```bash
# 1. Create environment file
cat > .env << EOF
SERPAPI_API_KEY=your_serpapi_key_here
HUGGINGFACE_API_KEY=your_huggingface_key_here
EOF

# 2. Start the service
docker-compose up -d

# 3. Test it
curl http://localhost:8000/health
```

### Option 2: Local Development

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set environment variables
export SERPAPI_API_KEY=your_serpapi_key
export HUGGINGFACE_API_KEY=your_huggingface_key

# 3. Run the API server
uvicorn api:app --host 0.0.0.0 --port 8000

# Or run the CLI version
python main.py
```

## 📡 API Endpoints

### POST /research

Perform web research and get AI-summarized results.

**Request:**
```json
{
  "query": "best machine learning frameworks for beginners"
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "results": [
      {
        "rank": 1,
        "title": "Top Machine Learning Frameworks for Beginners",
        "url": "https://example.com/ml-frameworks",
        "summary": "TensorFlow and PyTorch are the most popular frameworks for beginners. TensorFlow offers extensive documentation while PyTorch provides intuitive syntax..."
      },
      {
        "rank": 2,
        "title": "Getting Started with Scikit-learn",
        "url": "https://example.com/scikit-learn",
        "summary": "Scikit-learn is the perfect starting point for beginners with classical ML algorithms..."
      }
    ]
  }
}
```

### GET /health

Health check endpoint for monitoring.

**Response:**
```json
{
  "status": "healthy"
}
```

### GET /

Service information and version.

**Response:**
```json
{
  "service": "Research Agent API",
  "status": "running",
  "version": "1.0.0"
}
```

## 🔧 Configuration

Environment variables (`.env` file):

```bash
# Required
SERPAPI_API_KEY=your_serpapi_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key

# Optional (with defaults)
HUGGINGFACE_API_BASE=https://router.huggingface.co/v1
LLAMA_MODEL_NAME=meta-llama/Llama-3.3-70B-Instruct
DEFAULT_TEMPERATURE=0.7
DEFAULT_MAX_TOKENS=2048
```

### Getting API Keys

**SerpAPI (Web Search):**
1. Visit [serpapi.com](https://serpapi.com/)
2. Sign up for a free account (100 searches/month)
3. Copy your API key from the dashboard

**HuggingFace (AI Model):**
1. Visit [huggingface.co](https://huggingface.co/)
2. Create an account and go to Settings → Access Tokens
3. Create a new token with read permissions
4. Optional: Add payment method for higher rate limits

## 📚 Documentation

- [QUICKSTART.md](./QUICKSTART.md) - Get started in 3 steps
- [README.Docker.md](./README.Docker.md) - Detailed Docker deployment guide
- [example_client.py](./example_client.py) - Python client usage examples
- [test_api.py](./test_api.py) - API testing script

## 🧪 Testing

### Test the API

```bash
# Using test script
python test_api.py

# With custom query
python test_api.py "your research query here"

# Using curl
curl -X POST http://localhost:8000/research \
  -H "Content-Type: application/json" \
  -d '{"query": "latest AI trends 2024"}'

# Interactive API docs
open http://localhost:8000/docs
```

### Test the CLI

```bash
# Run interactive CLI
python main.py

# Enter queries interactively
Query: best Python web frameworks
```

### Example Client

```bash
# Run the example client
python example_client.py
```

## 🛠️ Development

### Project Structure

```
research assistant/
├── agents/
│   └── research.py              # Main research agent logic
├── chains/
│   └── summary.py               # AI summarization chain
├── tools/
│   └── web_search.py            # SerpAPI web search tool
├── utils/
│   ├── config.py                # Configuration management
│   └── logger.py                # Logging setup
├── tests/                       # Unit and integration tests
│   ├── test_agent.py
│   ├── test_summary.py
│   └── test_web_search.py
├── logs/                        # Application logs
├── api.py                       # FastAPI application
├── main.py                      # CLI entry point
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker image definition
└── docker-compose.yml           # Container orchestration
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_agent.py

# Run with coverage
pytest --cov=. tests/
```

### Viewing Logs

```bash
# Docker logs
docker-compose logs -f

# Local logs (in logs/ directory)
tail -f logs/research_assistant_*.log
```

## 🔗 Dependencies

**Core Technologies:**
- **FastAPI**: Modern Python web framework
- **LangChain**: AI/LLM orchestration framework
- **SerpAPI**: Google search API
- **Llama 3.3 70B**: AI model via HuggingFace
- **Uvicorn**: ASGI server

**Key Python Packages:**
- `langchain` - LLM framework
- `langchain-openai` - OpenAI-compatible LLM interface
- `serpapi` - Web search integration
- `fastapi` - REST API framework
- `pydantic` - Data validation

## 🐛 Troubleshooting

### API Returns 500 Errors

**Check logs:**
```bash
# Docker
docker-compose logs -f research-agent

# Local
cat logs/research_assistant_*.log
```

**Common causes:**
- Invalid API keys
- API rate limits exceeded
- Network connectivity issues

### No Search Results

**Verify SerpAPI key:**
```bash
curl "https://serpapi.com/search?q=test&api_key=YOUR_KEY"
```

**Check remaining credits:**
- Visit [serpapi.com/manage](https://serpapi.com/manage)
- Verify you have remaining searches

### Container Won't Start

**Check if port 8000 is available:**
```bash
# Linux/Mac
lsof -i :8000

# Windows
netstat -ano | findstr :8000
```

**Verify environment file exists:**
```bash
ls -la .env
cat .env
```

**Rebuild container:**
```bash
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### LLM Errors

**Rate limiting:**
- HuggingFace free tier has rate limits
- Consider upgrading or adding payment method
- Check [huggingface.co/pricing](https://huggingface.co/pricing)

**Model unavailable:**
- Verify model name in configuration
- Check HuggingFace service status

## 🌟 Use Cases

- **Content Research**: Gather information on any topic
- **Market Research**: Analyze trends and competitors
- **Technical Documentation**: Find solutions and best practices
- **News Aggregation**: Get latest news with summaries
- **Academic Research**: Quick literature review starting points
- **Product Research**: Compare products and reviews

## 🔄 Integration Examples

### Python Client

```python
import requests

def research(query):
    response = requests.post(
        "http://localhost:8000/research",
        json={"query": query}
    )
    return response.json()

# Use it
results = research("best Python IDE")
for result in results['data']['results']:
    print(f"{result['rank']}. {result['title']}")
    print(f"   {result['summary']}\n")
```

### JavaScript/Node.js Client

```javascript
async function research(query) {
  const response = await fetch('http://localhost:8000/research', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query })
  });
  return await response.json();
}

// Use it
const results = await research('latest web development trends');
console.log(results.data.results);
```

### Using as a Service

The Research Assistant can serve as a backend service for:
- Other AI agents (like Budget Context7 Agent)
- Web applications requiring research capabilities
- Slack/Discord bots
- Chrome extensions
- Mobile apps

## 📈 Performance

**Typical Response Times:**
- Web search: 1-2 seconds
- AI summarization: 2-4 seconds
- **Total**: 3-6 seconds per query

**Rate Limits:**
- SerpAPI free tier: 100 searches/month
- HuggingFace free tier: Rate limited (varies)
- Consider upgrading for production use

## 🔒 Security

- **API Keys**: Never commit `.env` file to version control
- **Network**: Consider adding authentication for production
- **Docker**: Runs as non-root user by default
- **Logs**: Sensitive data is not logged

## 🚀 Production Deployment

### Using Docker Compose

```bash
# Production docker-compose.yml
docker-compose -f docker-compose.yml up -d
```

### Using Kubernetes

```bash
# Create secrets
kubectl create secret generic research-agent-secrets \
  --from-literal=SERPAPI_API_KEY=your_key \
  --from-literal=HUGGINGFACE_API_KEY=your_key

# Deploy
kubectl apply -f k8s/deployment.yaml
```

### Environment Variables for Production

```bash
# Increase worker count
UVICORN_WORKERS=4

# Production logging
LOG_LEVEL=INFO

# Timeouts
REQUEST_TIMEOUT=30
```

## 📝 License

MIT License - See LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/research-assistant/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/research-assistant/discussions)
- **Email**: your.email@example.com

## 🙏 Acknowledgments

- **LangChain** - AI orchestration framework
- **SerpAPI** - Web search API
- **Meta AI** - Llama 3.3 70B model
- **HuggingFace** - Model hosting and inference
- **FastAPI** - Web framework

---

Made with ❤️ by [Your Name]

