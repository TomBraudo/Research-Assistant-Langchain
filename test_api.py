#!/usr/bin/env python3
"""
Simple test script for the Research Agent API
Run this after starting the Docker container to verify the API is working
"""

import requests
import json
import sys

API_URL = "http://localhost:8000"

def test_health():
    """Test the health endpoint"""
    print("🏥 Testing health endpoint...")
    try:
        response = requests.get(f"{API_URL}/health")
        response.raise_for_status()
        print(f"✅ Health check passed: {response.json()}")
        return True
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_research(query: str):
    """Test the research endpoint"""
    print(f"\n🔍 Testing research endpoint with query: '{query}'")
    try:
        response = requests.post(
            f"{API_URL}/research",
            json={"query": query},
            timeout=60  # Research can take a while
        )
        response.raise_for_status()
        
        data = response.json()
        print("✅ Research completed successfully!")
        print("\n📊 Results:")
        print(json.dumps(data, indent=2))
        
        return True
    except requests.exceptions.Timeout:
        print("❌ Request timed out (this might be normal for first request)")
        return False
    except Exception as e:
        print(f"❌ Research failed: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response: {e.response.text}")
        return False

def main():
    print("=" * 60)
    print("Research Agent API Test")
    print("=" * 60)
    
    # Test health endpoint
    if not test_health():
        print("\n❌ API is not running. Please start the Docker container:")
        print("   docker-compose up -d")
        sys.exit(1)
    
    # Test research endpoint
    test_query = "best Python libraries for machine learning"
    if len(sys.argv) > 1:
        test_query = " ".join(sys.argv[1:])
    
    test_research(test_query)
    
    print("\n" + "=" * 60)
    print("Test completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()

