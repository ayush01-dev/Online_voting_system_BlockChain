#!/bin/bash

# OVS 2.0 Setup Script
echo "🗳️  Setting up OVS 2.0 - Online Voting System using Blockchain"
echo "=============================================================="

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}' | cut -d'.' -f1,2)
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python 3.8 or higher is required. Current version: $python_version"
    exit 1
fi

echo "✅ Python version check passed: $python_version"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Copy environment template
echo "⚙️  Setting up environment configuration..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "✅ Created .env file from template"
    echo "⚠️  Please edit .env file with your email credentials"
else
    echo "⚠️  .env file already exists, skipping..."
fi

# Setup config files
echo "🏢 Setting up configuration files..."
if [ ! -f config/organizations.txt ]; then
    cp config/organizations.example.txt config/organizations.txt
    echo "✅ Created organizations.txt from example"
else
    echo "⚠️  organizations.txt already exists, skipping..."
fi

if [ ! -f Varified_gmail_and_password/users.json ]; then
    cp Varified_gmail_and_password/users.example.json Varified_gmail_and_password/users.json
    echo "✅ Created users.json from example"
else
    echo "⚠️  users.json already exists, skipping..."
fi

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "📝 Next steps:"
echo "1. Edit .env file with your email credentials for OTP service"
echo "2. Update config/organizations.txt with your organizations"
echo "3. Run 'python main.py' to start the voting system"
echo "4. Visit http://localhost:8000 to access the voting interface"
echo ""
echo "📖 For detailed instructions, see INSTALLATION.md"
echo "📚 For API documentation, see API_DOCUMENTATION.md"
echo ""
echo "Happy voting! 🗳️"