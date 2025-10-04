# 🤝 Contributing to Debezium Real-Time Chat

Thank you for your interest in contributing to this project! This guide will help you get started.

## 🎯 About the Project

This is a real-time chat project that uses **Debezium CDC (Change Data Capture)** to capture changes in the PostgreSQL database and distribute these changes via WebSockets to all connected clients.

**🎓 Perfect for Learning CDC!** This project serves as an excellent educational resource for understanding Change Data Capture concepts, real-time data streaming, and modern event-driven architectures.

### 🏗️ Architecture
```
PostgreSQL → Debezium → Kafka → FastAPI → WebSocket → Frontend
```

## 🚀 Getting Started

### 1. Fork and Clone
```bash
git clone https://github.com/YOUR_USERNAME/debezium.git
cd debezium
```

### 2. Environment Setup
```bash
# Install dependencies
make build

# Start services
make up

# Verify everything is working
curl http://localhost:8000
```

### 3. Project Structure
```
debezium/
├── app/                    # Main application code
│   ├── internal/          # Internal logic (consumer, connection manager)
│   ├── routes/            # API routes
│   ├── static/            # Static files (CSS, JS)
│   ├── templates/         # HTML templates
│   ├── main.py           # Application entry point
│   └── settings.py       # Configuration
├── docs/                 # Documentation
├── .github/              # Templates and workflows
└── docker-compose.yaml   # Docker services
```

## 🎨 Types of Contributions

### 🐛 Bug Fixes
- Fix existing issues
- Improve error handling
- Optimize performance

### ✨ New Features
- Authentication system
- Chat rooms
- File uploads
- Push notifications
- Metrics dashboard

### 📚 Documentation
- Improve README
- Add examples
- Create tutorials
- Document APIs

### 🎨 UI/UX
- Improve interface
- Add themes
- Make it responsive
- Animations

### 🧪 Testing
- Unit tests
- Integration tests
- E2E tests
- Coverage

## 🔧 Development Tools

### Useful Commands
```bash
make build          # Build application
make up             # Start services
make down           # Stop services
make logs           # View logs
make linter         # Check code
make format         # Format code
```

### Tech Stack
- **Backend**: Python 3.12+, FastAPI
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Database**: PostgreSQL
- **Message Broker**: Apache Kafka
- **CDC**: Debezium (Learn CDC concepts through hands-on practice!)
- **Containerization**: Docker & Docker Compose

### 🎓 Educational Value
This project is designed to help developers learn:
- **Change Data Capture (CDC)** fundamentals
- **Event-driven architecture** patterns
- **Real-time data streaming** concepts
- **Microservices communication** via message brokers
- **WebSocket** implementations
- **Database replication** techniques

## 📝 Code Standards

### Python
- Use `ruff` for formatting and linting
- Follow PEP 8
- Document complex functions
- Use type hints when possible

### Frontend
- Clean and commented JavaScript code
- Modular and responsive CSS
- Semantic HTML

### Commits
Use Conventional Commits pattern:
```
feat: add authentication system
fix: fix WebSocket reconnection issue
docs: update README with new instructions
style: improve chat layout
refactor: reorganize folder structure
test: add tests for consumer
```

## 🐛 Reporting Bugs

1. Check if a similar issue already exists
2. Use the bug report template
3. Include relevant logs
4. Describe steps to reproduce

## ✨ Suggesting Features

1. Check if a similar issue already exists
2. Use the feature request template
3. Explain the problem it solves
4. Include mockups if possible

## 🎉 Pull Request Process

1. **Create a branch** for your feature/fix:
   ```bash
   git checkout -b feature/new-feature
   ```

2. **Make your changes** following the standards

3. **Test your changes**:
   ```bash
   make linter
   make test  # when implemented
   ```

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/new-feature
   ```

6. **Open a Pull Request** with:
   - Clear description of changes
   - Screenshots (if applicable)
   - Reference to issue (if any)

## 🏷️ Issue Labels

- `good first issue` - Great for beginners
- `hacktoberfest` - Issues for Hacktoberfest
- `bug` - Problems to be fixed
- `enhancement` - Improvements and new features
- `documentation` - Documentation improvements
- `help wanted` - Needs community help

## 🎯 Recommended Issues for Beginners

- Improve CSS styles
- Add frontend validations
- Create unit tests
- Improve documentation
- Add more detailed logs

## 💬 Communication

- Use issues for technical discussions
- Be respectful and constructive
- Help other contributors
- Share knowledge

## 📜 Code of Conduct

This project follows the [Contributor Covenant](CODE_OF_CONDUCT.md). By participating, you agree to uphold this code.

## 🆘 Need Help?

- Open an issue with the `question` label
- Use the Hacktoberfest template discussion
- Contact the maintainers

---

**Thank you for contributing! 🚀**

Every contribution, no matter how small, makes a difference!
