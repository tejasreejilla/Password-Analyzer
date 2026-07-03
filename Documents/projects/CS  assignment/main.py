"""
Password Strength Analyzer - Main Entry Point
Run this file to start the web application
"""

import webbrowser
import os

if __name__ == "__main__":
    print("🔐 Starting Password Strength Analyzer...")
    print("Opening web interface in your browser...\n")
    
    # Get the path to index.html
    current_dir = os.path.dirname(os.path.abspath(__file__))
    html_file = os.path.join(current_dir, "index.html")
    
    # Open in default browser
    webbrowser.open('file://' + html_file)
    
    print("✅ Web interface opened!")
    print("If the browser didn't open, manually open: index.html")
