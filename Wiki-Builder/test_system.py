# test_system.py - Test the complete multi-agent system

from crew import run_crew
import os
from dotenv import load_dotenv

load_dotenv()

def test_multi_agent_system():
    """Test the complete 3-agent system"""

    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in environment variables")
        return False

    print("🤖 Testing Multi-Agent Wikipedia Builder")
    print("=" * 50)
    print("Testing with topic: 'Artificial Intelligence'")
    print()

    try:
        result = run_crew("Artificial Intelligence")

        print("✅ Multi-agent system completed successfully!")
        print(f"📄 Generated content length: {len(result)} characters")

        # Check for Wikipedia-style formatting
        if "# " in result and "## " in result:
            print("✅ Proper Wikipedia formatting detected!")
        else:
            print("⚠️  Wikipedia formatting may need adjustment")

        # Show preview
        preview = result[:300] + "..." if len(result) > 300 else result
        print("\n📋 Content preview:")
        print("-" * 30)
        print(preview)
        print("-" * 30)

        return True

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_multi_agent_system()

    if success:
        print("\n🎉 System is ready! Run: streamlit run main.py")
    else:
        print("\n🔧 Please check your setup and try again")
