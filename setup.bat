@echo off
echo 🗳️  Setting up OVS 2.0 - Online Voting System using Blockchain
echo ==============================================================

REM Check Python version
python --version > python_version.txt 2>&1
for /f "tokens=2" %%i in (python_version.txt) do set python_version=%%i
del python_version.txt

echo ✅ Python version: %python_version%

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔌 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📚 Installing dependencies...
pip install -r requirements.txt

REM Copy environment template
echo ⚙️  Setting up environment configuration...
if not exist .env (
    copy .env.example .env
    echo ✅ Created .env file from template
    echo ⚠️  Please edit .env file with your email credentials
) else (
    echo ⚠️  .env file already exists, skipping...
)

REM Setup config files
echo 🏢 Setting up configuration files...
if not exist config\organizations.txt (
    copy config\organizations.example.txt config\organizations.txt
    echo ✅ Created organizations.txt from example
) else (
    echo ⚠️  organizations.txt already exists, skipping...
)

if not exist Varified_gmail_and_password\users.json (
    copy Varified_gmail_and_password\users.example.json Varified_gmail_and_password\users.json
    echo ✅ Created users.json from example
) else (
    echo ⚠️  users.json already exists, skipping...
)

echo.
echo 🎉 Setup completed successfully!
echo.
echo 📝 Next steps:
echo 1. Edit .env file with your email credentials for OTP service
echo 2. Update config\organizations.txt with your organizations
echo 3. Run 'python main.py' to start the voting system
echo 4. Visit http://localhost:8000 to access the voting interface
echo.
echo 📖 For detailed instructions, see INSTALLATION.md
echo 📚 For API documentation, see API_DOCUMENTATION.md
echo.
echo Happy voting! 🗳️
pause