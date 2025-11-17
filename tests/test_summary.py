"""
Test script for the summary chain
Tests the updated LangChain v1.0 implementation
"""
import sys
import os

# Add parent directory to path so we can import from chains
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from langchain_core.documents import Document
from chains.summary import summarize_documents

def test_summarization():
    """Test the summarize_documents function with sample content"""
    print("=" * 60)
    print("Testing Summary Chain")
    print("=" * 60)
    print()
    
    # Create sample documents to summarize
    sample_text = """
    Python continues to dominate as one of the most popular programming languages in 2025.
    Its versatility in web development, data science, machine learning, and automation makes it 
    a top choice for developers worldwide. Python's extensive library ecosystem and readable 
    syntax contribute to its widespread adoption.
    
    JavaScript remains essential for web development, powering both frontend and backend 
    applications through frameworks like React, Vue, and Node.js. Its ubiquity in web browsers 
    and growing use in mobile development keeps it highly relevant.
    
    TypeScript has seen tremendous growth, offering static typing on top of JavaScript. 
    Many large-scale applications now prefer TypeScript for its better tooling, error detection,
    and maintainability. Major frameworks like Angular and Vue have embraced TypeScript.
    
    Go (Golang) is favored for cloud-native applications, microservices, and backend systems.
    Its performance, simplicity, and built-in concurrency support make it ideal for modern 
    infrastructure and DevOps tools. Companies like Google, Uber, and Docker rely heavily on Go.
    
    Rust continues to gain popularity for systems programming, offering memory safety without 
    garbage collection. Its use in performance-critical applications, WebAssembly, and even 
    parts of major operating systems demonstrates its growing importance in 2025.
    """
    
    # Create a Document object
    docs = [Document(page_content=sample_text)]
    
    print("Sample Text (truncated):")
    print(sample_text[:200] + "...\n")
    print("-" * 60)
    print()
    print("Generating 5-bullet summary using Llama 3.3 70B...")
    print()
    
    # Call the summarize_documents function
    summary = summarize_documents(docs)
    
    # Print the results
    print("📝 Summary Result:")
    print("-" * 60)
    print(summary)
    print()
    print("=" * 60)
    print("Test completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    test_summarization()

