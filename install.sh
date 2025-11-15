#!/usr/bin/env bash
set -e

echo "🔧 Installing dependencies for Mentalist v2.0..."
sudo apt update -y

# Core Python dependencies
sudo apt install -y python3 python3-pip python3-tk

# Optional text parsers and command-line tools
sudo apt install -y lynx pandoc html2text

# Python packages required by the new features
pip install --upgrade pip
pip install requests beautifulsoup4

echo "✅ Installation complete."
echo "To run Mentalist v2.0:"
echo "  PYTHONPATH=. python3 -m mentalist"
