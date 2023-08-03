import requests

headers = {"Content-Type": "application/json"} 
pload = {"sentences": ["this is a test sentence", "nackte vagines, drogen und schnaps"]}
r = requests.post("http://localhost:5001/sentences2embeddings", json=pload, headers=headers)
print(r.text)
