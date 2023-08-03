### Local Setup Instructions

Requirements:
- python >3.7
- docker
- docker-compose

```bash
# Clone project
git clone https://github.com/fipso/ml-itdz.git
cd ml-itdz

# Run dependency services: Milvus Vector DB & React Chat Frontend
docker-compose up -d

# Create venv and install python deps
python -m venv venv
pip install -r requirements.txt

# Run AI Backend
chmod +x chat_service.py
./chat_service

# Visit Chat Frontend at http://127.0.0.1:3000
```
