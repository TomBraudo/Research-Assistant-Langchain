#!/usr/bin/env python3
"""
Example client showing how other agents/services can call the Research Agent API
This demonstrates the decoupled architecture where other services can use this agent
"""

import requests
from typing import Optional, List, Dict

class ResearchAgentClient:
    """Client for interacting with the Research Agent API"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        """
        Initialize the client
        
        Args:
            base_url: Base URL of the Research Agent API
        """
        self.base_url = base_url.rstrip('/')
    
    def health_check(self) -> bool:
        """
        Check if the Research Agent API is healthy
        
        Returns:
            bool: True if API is healthy, False otherwise
        """
        try:
            response = requests.get(f"{self.base_url}/health", timeout=5)
            return response.status_code == 200
        except Exception:
            return False
    
    def research(self, query: str, timeout: int = 60) -> Optional[Dict]:
        """
        Perform research using the Research Agent
        
        Args:
            query: The search query
            timeout: Request timeout in seconds
            
        Returns:
            Dict with research results or None if failed
        """
        try:
            response = requests.post(
                f"{self.base_url}/research",
                json={"query": query},
                timeout=timeout
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error calling Research Agent: {e}")
            return None
    
    def get_top_result(self, query: str) -> Optional[Dict]:
        """
        Get just the top research result
        
        Args:
            query: The search query
            
        Returns:
            Dict with the top result or None
        """
        results = self.research(query)
        if results and results.get("status") == "success":
            data = results.get("data", {})
            results_list = data.get("results", [])
            if results_list:
                return results_list[0]
        return None
    
    def get_all_results(self, query: str) -> List[Dict]:
        """
        Get all research results
        
        Args:
            query: The search query
            
        Returns:
            List of result dictionaries
        """
        results = self.research(query)
        if results and results.get("status") == "success":
            data = results.get("data", {})
            return data.get("results", [])
        return []


def main():
    """Example usage of the Research Agent Client"""
    
    # Initialize client
    client = ResearchAgentClient()
    
    # Check health
    print("Checking API health...")
    if not client.health_check():
        print("❌ Research Agent API is not available!")
        print("Make sure it's running: docker-compose up -d")
        return
    
    print("✅ API is healthy\n")
    
    # Example 1: Get all results
    print("=" * 60)
    print("Example 1: Get all research results")
    print("=" * 60)
    
    query = "best Python data visualization libraries"
    print(f"Query: {query}\n")
    
    results = client.get_all_results(query)
    
    if results:
        print(f"Found {len(results)} results:\n")
        for result in results:
            print(f"#{result['rank']}: {result['title']}")
            print(f"   URL: {result['url']}")
            print(f"   Summary: {result['summary'][:100]}...")
            print()
    else:
        print("No results found")
    
    # Example 2: Get just the top result
    print("\n" + "=" * 60)
    print("Example 2: Get only the top result")
    print("=" * 60)
    
    query = "FastAPI vs Flask comparison"
    print(f"Query: {query}\n")
    
    top_result = client.get_top_result(query)
    
    if top_result:
        print(f"Top Result: {top_result['title']}")
        print(f"URL: {top_result['url']}")
        print(f"Summary: {top_result['summary']}")
    else:
        print("No results found")


if __name__ == "__main__":
    main()

