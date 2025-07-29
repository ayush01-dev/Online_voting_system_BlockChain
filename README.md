# OVS 2.0 - Online Voting System using Blockchain

A secure, transparent, and decentralized online voting system built with blockchain technology to ensure vote integrity and prevent tampering.

## 🚀 Features

- **Blockchain-based Security**: Custom blockchain implementation with SHA-256 hashing and proof-of-work consensus
- **Email OTP Verification**: Secure user registration with email-based OTP verification
- **Admin Panel**: Token-based administrative interface for managing organizations and voting sessions
- **Organization Management**: Dynamic addition and removal of participating organizations
- **Real-time Vote Tracking**: Live vote counting with blockchain verification
- **Tamper-proof Results**: Immutable vote records stored on blockchain
- **Web Interface**: User-friendly web interface for voting and administration

## 🏗️ Architecture

The system consists of several key components:

### Core Components
- **FastAPI Server** (`main.py`): Main application server handling voting logic
- **Blockchain Engine** (`blockchainfolder/chain.py`): Custom blockchain implementation
- **User Registration** (`Varified_gmail_and_password/`): Flask-based OTP verification system
- **Web Interface** (`templates/`, `static/`): HTML/CSS frontend

### Data Storage
- **User Database**: JSON-based user storage with encrypted passwords
- **Organization Config**: Text-based configuration for participating organizations
- **Blockchain Data**: In-memory blockchain with persistent vote records

## 📋 Prerequisites

- Python 3.8 or higher
- Gmail account for OTP email service (or SMTP server)
- Internet connection for email verification

## 🛠️ Installation

### Quick Setup (Recommended)

**Linux/macOS:**
```bash
git clone https://github.com/Akashbht/OVS_2.O.git
cd OVS_2.O
./setup.sh
```

**Windows:**
```bash
git clone https://github.com/Akashbht/OVS_2.O.git
cd OVS_2.O
setup.bat
```

### Manual Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Akashbht/OVS_2.O.git
   cd OVS_2.O
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure email settings**
   ```bash
   cp .env.example .env
   # Edit .env with your email credentials
   ```

4. **Set up configuration files**
   ```bash
   cp config/organizations.example.txt config/organizations.txt
   cp Varified_gmail_and_password/users.example.json Varified_gmail_and_password/users.json
   ```

## 🚀 Usage

### Starting the Application

1. **Start the main voting server**
   ```bash
   python main.py
   ```
   The server will start on `http://localhost:8000`

2. **Start the registration server** (optional, for new user registration)
   ```bash
   cd Varified_gmail_and_password
   python server.py
   ```
   Registration server will start on `http://localhost:5000`

### Admin Operations

1. **Access Admin Panel**
   - Navigate to `http://localhost:8000/admin`
   - Use the admin token displayed in the console

2. **Managing Organizations**
   - Add new organizations via the admin panel
   - Delete organizations using the admin interface

3. **Controlling Voting**
   - Start voting session: POST to `/admin/start` with admin token
   - Stop voting session: POST to `/admin/stop` with admin token

### Voting Process

1. **User Registration** (if not already registered)
   - Visit registration portal
   - Provide email, name, age, and password
   - Verify email via OTP

2. **Casting Vote**
   - Navigate to the main voting page
   - Enter user credentials
   - Select organization using organization code
   - Submit vote (creates blockchain entry)

3. **View Results**
   - Access `/getvotes` for total vote count
   - Access `/getvotesbyorg` for organization-wise results (after voting ends)

## 🔧 API Endpoints

### Voting Endpoints
- `GET /` - Main voting interface
- `POST /voter/vote` - Cast a vote
- `GET /getOrgDetail` - Get organization details

### Admin Endpoints
- `GET /admin` - Admin panel interface
- `POST /admin/login` - Admin authentication
- `POST /admin/start` - Start voting session
- `POST /admin/stop` - Stop voting session
- `POST /admin/add_organization` - Add new organization
- `POST /admin/delete_organization` - Remove organization

### Results Endpoints
- `GET /getvotes` - Get total vote count
- `GET /getvotesbyorg` - Get votes by organization

## 🔐 Security Features

- **Blockchain Integrity**: Each vote creates a new block with cryptographic hash
- **Proof of Work**: Mining difficulty ensures computational cost for tampering
- **User Authentication**: Email verification and password protection
- **Admin Security**: Token-based administrative access
- **Vote Immutability**: Once cast, votes cannot be modified or deleted

## 📁 Project Structure

```
OVS_2.O/
├── main.py                          # Main FastAPI application
├── requirements.txt                 # Python dependencies
├── Procfile                        # Heroku deployment configuration
├── blockchainfolder/
│   └── chain.py                    # Blockchain implementation
├── Varified_gmail_and_password/
│   ├── server.py                   # Flask registration server
│   ├── otp.py                      # OTP generation and email
│   ├── users.json                  # User database
│   └── templates/                  # Registration templates
├── templates/                      # Main app HTML templates
│   ├── item.html                   # Voting interface
│   ├── confirm.html               # Vote confirmation
│   ├── admin_login.html           # Admin login
│   └── admin_panel.html           # Admin dashboard
├── static/                         # CSS and static files
│   ├── style.css                   # Main styling
│   └── confirm.css                 # Confirmation page styling
├── config/                         # Configuration files
│   ├── organizations.txt           # Organization data
│   └── token.txt                   # Admin token
├── dbfolder/
│   └── userdata.py                 # Additional user data
├── utils.py                        # Utility functions
├── user_data.py                    # User data management
├── otp.py                          # OTP utilities
└── test.py                         # Blockchain testing
```

## 🧪 Testing

Run the blockchain test to verify functionality:
```bash
python test.py
```

## 🌐 Deployment

The application is ready for deployment on platforms like Heroku:
1. Ensure `Procfile` is configured correctly
2. Set environment variables for email configuration
3. Deploy using your preferred platform

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🛡️ Disclaimer

This is an educational project demonstrating blockchain concepts in voting systems. For production use, additional security measures and extensive testing would be required.

## 👥 Authors

- **Akashbht** - *Initial work* - [Akashbht](https://github.com/Akashbht)

## 🔗 Links

- [Repository](https://github.com/Akashbht/OVS_2.O)
- [Issues](https://github.com/Akashbht/OVS_2.O/issues)
- [Pull Requests](https://github.com/Akashbht/OVS_2.O/pulls)
