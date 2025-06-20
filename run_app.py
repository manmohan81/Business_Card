"""
Alternative runner script for the Streamlit business card application.
This can be used if you prefer to run the app with additional configurations.
"""

import subprocess
import sys
import os

def run_streamlit_app():
    """Run the Streamlit application with custom configuration."""
    
    # Check if streamlit is installed
    try:
        import streamlit
        print("✅ Streamlit is installed")
    except ImportError:
        print("❌ Streamlit not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])
        print("✅ Streamlit installed successfully")
    
    # Configuration options
    config_options = [
        "--server.port=8501",
        "--server.address=0.0.0.0",
        "--server.headless=false",
        "--browser.gatherUsageStats=false",
        "--theme.primaryColor=#2563eb",
        "--theme.backgroundColor=#0f172a",
        "--theme.secondaryBackgroundColor=#1e3a8a",
        "--theme.textColor=#ffffff"
    ]
    
    # Run the Streamlit app
    cmd = ["streamlit", "run", "streamlit_app.py"] + config_options
    
    print("🚀 Starting Streamlit Business Card Application...")
    print(f"📱 Open your browser to: http://localhost:8501")
    print("🛑 Press Ctrl+C to stop the application")
    
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error running application: {e}")

if __name__ == "__main__":
    run_streamlit_app()