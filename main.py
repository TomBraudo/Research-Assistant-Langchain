# Research Assistant - Main Entry Point
from agents.research_agent import research_agent

def main():
    """Main function to run the research assistant"""
    print("Research Assistant - Ready to help!")
    print("Type 'quit' or 'exit' to stop\n")
    
    while True:
        query = input("Enter your research query: ").strip()
        
        if query.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not query:
            continue
        
        try:
            # Run the agent with the user's query
            result = research_agent.invoke({"input": query})
            print("\n" + "="*50)
            print("RESULT:")
            print("="*50)
            print(result.get("output", result))
            print("="*50 + "\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()

