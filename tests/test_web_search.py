"""
Test script for the web_search tool
Tests the updated SerpAPI implementation
"""
import sys
import os

# Add parent directory to path so we can import from tools
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.web_search import web_search

def test_search():
    """Test the web_search tool with a sample query"""
    print("=" * 60)
    print("Testing Web Search Tool")
    print("=" * 60)
    print()
    
    query = "top 5 programming languages 2025"
    print(f"Query: {query}")
    print("-" * 60)
    print()
    
    # Call the web_search tool (use .invoke() for LangChain tools)
    results = web_search.invoke(query)
    
    # Print the results
    print("Results:")
    print(results)
    print()
    print("=" * 60)
    print("Test completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    test_search()

