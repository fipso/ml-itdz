from flask import Flask, request, jsonify
import logging
import requests
from langchain.document_loaders import PyPDFLoader
import os

headers = {"Content-Type": "application/json"}
app = Flask(__name__)

def split_pdf(path):
    doc_batch = []
    for filename in os.listdir(path):
        loader = PyPDFLoader(path + "/" + filename)
        pages = loader.load_and_split()
        batches = []
        for page in pages:
            #print("=" * 50)
            page_len = 0
            batch = ""
            for i in page.page_content.split("\n"):
                if (page_len + len(i)) > 500:
                    batches.append(batch)
                    batch = ""
                    page_len = 0
                page_len += len(i)
                batch += i + " "

        doc_batch.append(batches)
    return doc_batch


@app.route('/split_pdfs', methods=["POST"])
def split_pdfs():
    data = request.get_json()
    dir_path = data.get("dir_path", [])

    batches = split_pdf(dir_path)
    sentences = []
    for i in batches:
        sentences += i
    app.logger.info(sentences)
    pload = {'sentences': sentences}
    app.logger.info(pload)
    r = requests.post('http://localhost:5000/process_sentences', json=pload, headers=headers)
    return r.text

if __name__ == "__main__":
    app.run(debug=True, port=5005)
