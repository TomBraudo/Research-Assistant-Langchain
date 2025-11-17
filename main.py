from agents.research import research_with_summary
from utils.logger import get_logger

# Get logger for main
logger = get_logger("main")

def main():
    """
    Main entry point for the Research Assistant.
    Takes user input and runs the research agent to provide summarized results.
    """
    logger.info("Research Assistant started")
    print("🔍 Research Assistant")
    print("=" * 50)
    print("Enter your research query (or 'quit' to exit)")
    print()
    
    while True:
        try:
            # Get user input
            query = input("Query: ").strip()
            
            # Check for exit condition
            if query.lower() in ['quit', 'exit', 'q']:
                logger.info("User exited the application")
                print("👋 Goodbye!")
                break
            
            # Skip empty queries
            if not query:
                logger.warning("Empty query received")
                print("Please enter a valid query.")
                continue
            
            print(f"\n🔎 Researching: {query}")
            print("⏳ Searching and summarizing...")
            print("-" * 50)
            
            logger.info(f"User query received: '{query}'")
            
            # Run the research agent
            result = research_with_summary(query)
            
            # Print the results
            print("📝 Research Summary:")
            print(result)
            print("-" * 50)
            print()
            
            logger.info("Results displayed to user")
            
        except KeyboardInterrupt:
            logger.info("Application interrupted by user (Ctrl+C)")
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            logger.error(f"Error occurred: {str(e)}", exc_info=True)
            print(f"\n❌ Error: {str(e)}")
            print("Please try again with a different query.\n")

if __name__ == "__main__":
    main()
