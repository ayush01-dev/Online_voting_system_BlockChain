# Installation & Setup Guide

## System Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: 512MB RAM minimum
- **Storage**: 100MB free space
- **Internet**: Required for email OTP verification

## Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/Akashbht/OVS_2.O.git
cd OVS_2.O
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Basic Configuration
```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your email credentials
nano .env  # or use your preferred editor
```

### 4. Start the Application
```bash
python main.py
```

The application will be available at `http://localhost:8000`

## Detailed Setup

### Environment Setup

#### Using Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Using Conda
```bash
# Create conda environment
conda create -n ovs2 python=3.9
conda activate ovs2

# Install dependencies
pip install -r requirements.txt
```

### Email Configuration

#### Gmail Setup (Recommended)
1. **Enable 2-Factor Authentication**
   - Go to Google Account settings
   - Security → 2-Step Verification → Turn on

2. **Generate App Password**
   - Security → 2-Step Verification → App passwords
   - Select app: Mail
   - Select device: Other (custom name)
   - Copy the generated 16-character password

3. **Update Configuration**
   ```bash
   # In .env file
   SMTP_EMAIL=your-email@gmail.com
   SMTP_PASSWORD=your-16-char-app-password
   ```

#### Other Email Providers
```bash
# Outlook/Hotmail
SMTP_SERVER=smtp-mail.outlook.com
SMTP_PORT=587

# Yahoo
SMTP_SERVER=smtp.mail.yahoo.com
SMTP_PORT=587

# Custom SMTP
SMTP_SERVER=your-smtp-server.com
SMTP_PORT=587
```

### Organization Setup

#### Default Organizations
The system comes with default organizations in `config/organizations.txt`:
```
bjp:modi:345
inc:rahul:123
aap:kejriwal:8765
lol:abc:234
```

#### Adding Organizations
1. **Via Config File**:
   ```bash
   echo "newparty:leader:999" >> config/organizations.txt
   ```

2. **Via Admin Panel**:
   - Start the application
   - Access admin panel at `/admin`
   - Use the "Add Organization" form

#### Organization Format
```
Organization_Name:Leader_Name:Unique_Code
```

### User Registration Setup

#### Start Registration Server
```bash
cd Varified_gmail_and_password
python server.py
```
Access registration at `http://localhost:5000`

#### Manual User Addition
Edit `Varified_gmail_and_password/users.json`:
```json
{
  "user@example.com": {
    "name": "John Doe",
    "age": "25",
    "password": "userpassword"
  }
}
```

## Configuration Options

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| SMTP_EMAIL | Email for OTP service | - | Yes |
| SMTP_PASSWORD | Email password/app-password | - | Yes |
| SMTP_SERVER | SMTP server | smtp.gmail.com | No |
| SMTP_PORT | SMTP port | 587 | No |
| SECRET_KEY | Session secret key | auto-generated | No |
| ADMIN_TOKEN | Admin access token | auto-generated | No |
| HOST | Server host | 0.0.0.0 | No |
| PORT | Server port | 8000 | No |
| MINING_DIFFICULTY | Blockchain difficulty | 10 | No |

### Application Settings

#### Blockchain Configuration
- **Mining Difficulty**: Controls computational cost of mining blocks
- **Default**: 10 (takes ~1-5 seconds per vote)
- **Higher values**: More secure, slower voting
- **Lower values**: Less secure, faster voting

#### Security Settings
- **Admin Token**: Auto-generated on first run, stored in `config/token.txt`
- **Session Security**: Uses random secret key for session management
- **Password Storage**: Currently plaintext (improvement needed for production)

## Troubleshooting

### Common Issues

#### 1. Import Errors
```bash
# Error: ModuleNotFoundError
pip install -r requirements.txt

# If still failing, check Python version
python --version  # Should be 3.8+
```

#### 2. Email Issues
```bash
# Error: SMTP Authentication failed
# Solution: Use App Password instead of regular password
# Verify email credentials in .env file
```

#### 3. Port Already in Use
```bash
# Error: Address already in use
# Solution: Kill process or use different port
netstat -tulpn | grep :8000
kill -9 <process_id>

# Or change port in .env
PORT=8080
```

#### 4. Organizations Not Loading
```bash
# Error: At least two organisations should be registered
# Solution: Check organizations.txt format
cat config/organizations.txt

# Each line should be: name:leader:code
# Minimum 2 organizations required
```

#### 5. Permission Denied
```bash
# Error: Permission denied writing to config/
# Solution: Check file permissions
chmod 755 config/
chmod 644 config/*.txt
```

### Debug Mode

#### Enable Detailed Logging
```python
# In main.py, add:
import logging
logging.basicConfig(level=logging.DEBUG)
```

#### Check Application Status
```bash
# Test if server is running
curl http://localhost:8000/getOrgDetail

# Check admin token
cat config/token.txt
```

## Production Deployment

### Heroku Deployment
```bash
# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Set environment variables
heroku config:set SMTP_EMAIL=your-email@gmail.com
heroku config:set SMTP_PASSWORD=your-app-password

# Deploy
git push heroku main
```

### Docker Deployment
```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
# Build and run
docker build -t ovs2 .
docker run -p 8000:8000 -e SMTP_EMAIL=your-email ovs2
```

### Security Checklist for Production

- [ ] Use HTTPS/SSL certificates
- [ ] Hash user passwords
- [ ] Implement rate limiting
- [ ] Add input validation
- [ ] Use environment variables for secrets
- [ ] Enable audit logging
- [ ] Set up monitoring
- [ ] Configure firewall rules
- [ ] Use database instead of JSON files
- [ ] Implement backup strategy

## Support

### Getting Help
1. **Check Documentation**: README.md and API_DOCUMENTATION.md
2. **Common Issues**: Review troubleshooting section above
3. **GitHub Issues**: Report bugs or ask questions
4. **Email**: Contact repository maintainer

### Reporting Issues
When reporting issues, include:
- Operating system and Python version
- Full error message and stack trace
- Steps to reproduce the problem
- Configuration details (without sensitive data)

### Contributing
1. Fork the repository
2. Create feature branch
3. Follow coding standards
4. Add tests if applicable
5. Submit pull request with detailed description