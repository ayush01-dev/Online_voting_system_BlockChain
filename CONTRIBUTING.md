# Contributing to OVS 2.0

Thank you for your interest in contributing to the Online Voting System using Blockchain (OVS 2.0)! This document provides guidelines for contributing to the project.

## Code of Conduct

- Be respectful and professional in all interactions
- Welcome newcomers and help them get started
- Focus on constructive feedback and solutions
- Respect different viewpoints and experiences

## How to Contribute

### Reporting Issues

1. **Search existing issues** to avoid duplicates
2. **Use the issue template** if available
3. **Provide detailed information**:
   - Operating system and Python version
   - Steps to reproduce the issue
   - Expected vs actual behavior
   - Error messages and logs
   - Screenshots if applicable

### Suggesting Features

1. **Check if the feature already exists** or is planned
2. **Open a feature request issue** with:
   - Clear description of the feature
   - Use cases and benefits
   - Possible implementation approach
   - Any breaking changes

### Code Contributions

#### Getting Started

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/OVS_2.O.git
   cd OVS_2.O
   ```

2. **Set up development environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-number
   ```

#### Development Guidelines

##### Code Style
- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings for functions and classes
- Keep functions small and focused
- Use type hints where appropriate

##### Testing
- Add tests for new functionality
- Ensure existing tests pass
- Test edge cases and error conditions
- Include integration tests for API endpoints

##### Documentation
- Update README.md if needed
- Add/update API documentation
- Include code comments for complex logic
- Update CHANGELOG.md

#### Example Code Standards

```python
def calculate_vote_hash(voter_id: str, org_code: str) -> str:
    """
    Calculate blockchain hash for a vote.
    
    Args:
        voter_id: Unique identifier for the voter
        org_code: Organization code being voted for
        
    Returns:
        SHA-256 hash string
        
    Raises:
        ValueError: If voter_id or org_code is invalid
    """
    if not voter_id or not org_code:
        raise ValueError("voter_id and org_code are required")
    
    # Implementation here
    pass
```

#### Commit Guidelines

- Use clear, descriptive commit messages
- Start with a verb in imperative mood
- Reference issue numbers when applicable
- Keep commits focused and atomic

Examples:
```
Add user authentication validation
Fix blockchain hash verification bug
Update API documentation for /vote endpoint
Refs #123: Implement organization management
```

#### Pull Request Process

1. **Update documentation** as needed
2. **Add tests** for new functionality
3. **Ensure all tests pass**
   ```bash
   python -m pytest  # If tests exist
   python main.py    # Manual testing
   ```

4. **Create pull request** with:
   - Clear title and description
   - Link to related issues
   - Screenshots for UI changes
   - Test results

5. **Respond to feedback** promptly and professionally

### Areas for Contribution

#### High Priority
- **Security improvements**: Password hashing, input validation
- **Database integration**: Replace JSON files with proper database
- **Error handling**: Better error messages and logging
- **Testing**: Unit tests and integration tests
- **Performance**: Optimize blockchain operations

#### Medium Priority
- **UI/UX improvements**: Better web interface design
- **Mobile responsiveness**: Improve mobile experience
- **Monitoring**: Add health checks and metrics
- **Documentation**: More examples and tutorials

#### Low Priority
- **Additional features**: Vote analytics, audit trails
- **Integration**: External authentication providers
- **Deployment**: Kubernetes manifests, CI/CD pipelines

### Development Setup

#### Prerequisites
- Python 3.8+
- Git
- Email account for OTP testing

#### Local Development
```bash
# Clone and setup
git clone https://github.com/Akashbht/OVS_2.O.git
cd OVS_2.O
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your email credentials

# Start development server
python main.py
```

#### Testing Changes
```bash
# Manual testing
curl http://localhost:8000/getOrgDetail

# Test voting flow
# 1. Register users via registration server
# 2. Start voting via admin panel
# 3. Cast votes via main interface
# 4. Verify blockchain integrity
```

### Code Review Process

#### For Contributors
- Be open to feedback and suggestions
- Explain your approach and reasoning
- Test your changes thoroughly
- Update documentation as needed

#### For Reviewers
- Provide constructive feedback
- Focus on code quality and security
- Suggest improvements, not just problems
- Approve when ready, request changes if needed

### Community Guidelines

#### Communication
- Use GitHub issues for bug reports and feature requests
- Use pull requests for code discussions
- Be patient and helpful with newcomers
- Ask questions if anything is unclear

#### Recognition
- Contributors will be acknowledged in README.md
- Significant contributions may earn maintainer status
- All contributions are valued, regardless of size

### Getting Help

- **Documentation**: Check README.md and other docs first
- **Issues**: Search existing issues or create a new one
- **Contact**: Reach out to maintainers via GitHub

### Release Process

1. **Version numbering**: Follow semantic versioning (MAJOR.MINOR.PATCH)
2. **Changelog**: Update CHANGELOG.md with new features and fixes
3. **Testing**: Comprehensive testing of all features
4. **Documentation**: Update all relevant documentation
5. **Release**: Create GitHub release with notes

Thank you for contributing to OVS 2.0! Your efforts help make digital voting more secure and accessible.