import requests

headers ={"Content-Type": "application/json"}
pload = {"dir_path": "data2"}
r = requests.post("http://localhost:5005/split_pdfs", json=pload, headers=headers)
print(r.text)

