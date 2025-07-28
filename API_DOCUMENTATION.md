# API Documentation

## Overview
The OVS 2.0 API provides endpoints for managing a blockchain-based online voting system. The API is built with FastAPI and includes both user-facing voting endpoints and administrative functions.

## Base URL
```
http://localhost:8000
```

## Authentication
- **Admin endpoints**: Require admin token authentication
- **Voting endpoints**: Require user credentials (email/password)

## Endpoints

### Public Endpoints

#### GET /
**Description**: Main voting interface
**Response**: HTML voting page
**Content-Type**: text/html

#### GET /confirmation
**Description**: Vote confirmation page
**Response**: HTML confirmation page
**Content-Type**: text/html

#### GET /getOrgDetail
**Description**: Get list of organizations participating in voting
**Response**:
```json
{
  "orgNames": ["BJP", "INC", "AAP"],
  "leaderNames": ["Modi", "Rahul", "Kejriwal"],
  "orgCodes": ["345", "123", "8765"]
}
```

### Voting Endpoints

#### POST /voter/vote
**Description**: Cast a vote for an organization
**Content-Type**: application/x-www-form-urlencoded
**Request Body**:
```
userId=user@example.com
password=userpassword
orgCode=345
```
**Response**: HTML confirmation page with vote status

**Success Response**:
- Status: "successful"
- Returns blockchain hash for verification

**Error Responses**:
- "Voting is closed or it is not started"
- "Unregistered user"
- "wrong password"
- "you have already casted your vote"
- "Invalid Organisation Details"

### Admin Endpoints

#### GET /admin
**Description**: Admin panel interface
**Authentication**: Session-based (requires login)
**Response**: HTML admin dashboard

#### POST /admin/login
**Description**: Admin authentication
**Content-Type**: application/x-www-form-urlencoded
**Request Body**:
```
token=admin-token-here
```
**Response**: Redirect to admin panel or login error

#### POST /admin/start
**Description**: Start voting session
**Content-Type**: application/json
**Request Body**:
```json
{
  "token": "admin-token-here"
}
```
**Response**:
```json
{
  "status": "started"
}
```

#### POST /admin/stop
**Description**: Stop voting session
**Content-Type**: application/json
**Request Body**:
```json
{
  "token": "admin-token-here"
}
```
**Response**:
```json
{
  "status": "stopped"
}
```

#### POST /admin/add_organization
**Description**: Add new organization to voting
**Authentication**: Session-based
**Content-Type**: application/x-www-form-urlencoded
**Request Body**:
```
org_name=New Party
leader_name=Leader Name
org_code=999
```
**Response**:
```json
{
  "success": true
}
```
**Error Response**:
```json
{
  "error": "Organization code already exists"
}
```

#### POST /admin/delete_organization
**Description**: Remove organization from voting
**Authentication**: Session-based
**Content-Type**: application/json
**Request Body**:
```json
{
  "org_code": "999",
  "token": "admin-token-here"
}
```
**Response**:
```json
{
  "success": true
}
```

### Results Endpoints

#### GET /getvotes
**Description**: Get total vote count
**Response** (while voting is active):
```json
{
  "total_votes": 0,
  "status": "Voting is currently running"
}
```
**Response** (after voting ends):
```json
{
  "total_votes": 150,
  "status": "voting has been stopped"
}
```

#### GET /getvotesbyorg
**Description**: Get vote count by organization
**Note**: Only available after voting has ended
**Response** (while voting is active):
```json
{
  "status": "Voting is currently running"
}
```
**Response** (after voting ends):
```json
{
  "BJP": 85,
  "INC": 45,
  "AAP": 20
}
```

## Error Codes

### HTTP Status Codes
- **200**: Success
- **303**: Redirect (used for admin login)
- **400**: Bad Request
- **401**: Unauthorized
- **403**: Forbidden
- **404**: Not Found
- **500**: Internal Server Error

### Application Error Messages
- **"Not authenticated"**: Session expired or invalid
- **"Invalid token"**: Wrong admin token provided
- **"All fields are required"**: Missing required form fields
- **"Organization code already exists"**: Duplicate organization code
- **"Organization not found"**: Invalid organization code for deletion
- **"Voting is closed or it is not started"**: Voting session not active

## Data Models

### Organization
```json
{
  "name": "string",
  "leader": "string", 
  "code": "string"
}
```

### Vote
```json
{
  "userId": "string",
  "orgCode": "string",
  "hash": "string",
  "timestamp": "datetime"
}
```

### Block (Blockchain)
```json
{
  "data": "string",
  "previous_hash": "string",
  "hash": "string",
  "nonce": "number"
}
```

## Rate Limiting
- No explicit rate limiting implemented
- Natural limitation through blockchain mining process
- One vote per user enforced at application level

## Security Considerations
- Admin token should be kept secure
- User passwords are stored in plaintext (should be hashed in production)
- HTTPS recommended for production deployment
- Email verification required for user registration

## Examples

### Voting Workflow
1. **Get organizations**: `GET /getOrgDetail`
2. **Cast vote**: `POST /voter/vote`
3. **Confirm vote**: User sees confirmation page

### Admin Workflow
1. **Login**: `POST /admin/login`
2. **Start voting**: `POST /admin/start`
3. **Monitor**: `GET /admin` (admin panel)
4. **Stop voting**: `POST /admin/stop`
5. **View results**: `GET /getvotesbyorg`

### cURL Examples

**Get Organizations**:
```bash
curl -X GET http://localhost:8000/getOrgDetail
```

**Cast Vote**:
```bash
curl -X POST http://localhost:8000/voter/vote \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "userId=user@example.com&password=mypassword&orgCode=345"
```

**Start Voting (Admin)**:
```bash
curl -X POST http://localhost:8000/admin/start \
  -H "Content-Type: application/json" \
  -d '{"token": "your-admin-token"}'
```

**Get Results**:
```bash
curl -X GET http://localhost:8000/getvotesbyorg
```