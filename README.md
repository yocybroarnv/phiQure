# phiQure - Quantum-Safe Mail System

phiQure is a next-generation secure mail platform that combines Quantum Key Distribution (QKD) simulation, AI-driven threat detection, and modern cryptography.

## 🚀 Features

-  End-to-end encryption with QKD-derived keys
-  AI-powered phishing detection
-  BB84 quantum key exchange simulation
-  Real-time QBER monitoring
-  Zero-knowledge message storage
-  Anomaly detection and audit logging

## 🛠️ Tech Stack

- **Backend**: FastAPI + Python 3.11
- **Database**: PostgreSQL
- **Crypto**: AES-256 + HKDF
- **AI/ML**: Scikit-learn + TF-IDF
- **Frontend**: React + TypeScript
- **Container**: Docker + Docker Compose

## 🏗️ Setup & Development

### Prerequisites

- Python 3.11+
- Node.js 18+
- Docker and Docker Compose
- PostgreSQL 15+

### Quick Start

1. Clone the repository and set up environment:

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy example env and edit
cp .env.example .env
```

2. Start the database and backend:

```bash
# Start PostgreSQL and API via Docker
docker-compose up -d

# Apply database migrations
alembic upgrade head
```

3. Start development server:

```bash
# Start FastAPI development server
uvicorn app.main:app --reload --port 8000
```

4. Run tests:

```bash
# Run backend tests
pytest

# Run with coverage
pytest --cov=app tests/
```

## 🔒 Security Features

### Quantum Key Distribution (QKD)

- BB84 protocol simulation
- QBER monitoring and eavesdropping detection
- Key derivation via HKDF
- Ephemeral session keys

### AI Threat Detection

- TF-IDF + Logistic Regression for phishing detection
- Real-time anomaly monitoring
- Feature importance analysis
- Continuous model updates (optional)

### Cryptography

- AES-256-GCM for message encryption
- Forward secrecy with ephemeral keys
- Zero-knowledge message storage
- Secure key rotation

## 📚 API Documentation

Once running, visit:
- OpenAPI docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🧪 Development

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_qkd.py

# Run with coverage
pytest --cov=app --cov-report=html tests/
```

### Database Migrations

```bash
# Create new migration
alembic revision -m "description"

# Run migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

## 🐋 Docker Deployment

Build and run with Docker Compose:

```bash
# Build images
docker-compose build

# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## 🔍 Monitoring & Logs

Security events are logged to the `security_logs` table and include:
- Key exchange attempts
- High QBER incidents
- Phishing detections
- Authentication events

## 🚀 Future Enhancements

- [ ] Hardware QKD integration
- [ ] Federated learning for phishing detection
- [ ] Post-quantum cryptography upgrades
- [ ] Blockchain audit trail
- [ ] Multi-party key exchange

## 📝 License

MIT License - See LICENSE file

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## ⚠️ Security Notes

This is a demonstration system. While it implements real cryptographic primitives, the QKD portion is simulated. For production use:

- Replace QKD simulation with hardware
- Use proper HSM for key storage
- Enable additional security headers
- Implement rate limiting
- Add IP-based blocking

- Enable security audit logging

