"""
Test script for the research agent
Tests the updated LangChain v1.0 agent implementation
"""
import sys
import os

# Add parent directory to path so we can import from agents
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.research import research_with_summary

def test_research_agent():
    """Test the research agent with a sample query"""
    print("=" * 60)
    print("Testing Research Agent")
    print("=" * 60)
    print()
    
    # Sample research query
    query = "What are the latest developments in AI in 2025?"
    
    print(f"🔍 Research Query: {query}")
    print("-" * 60)
    print()
    print("⏳ Agent is searching the web and summarizing...")
    print()
    
    # Call the research agent
    try:
        summary = research_with_summary(query)
        
        # Print the results
        print("📝 Research Summary:")
        print("-" * 60)
        print(summary)
        print()
        print("=" * 60)
        print("✅ Test completed successfully!")
        print("=" * 60)
    except Exception as e:
        print(f"❌ Error during research: {str(e)}")
        print()
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_research_agent()

