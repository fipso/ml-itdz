from flask import Flask, request, jsonify, Response
import sys
from sentence_transformers import SentenceTransformer
import logging

app = Flask(__name__)

model = SentenceTransformer('sentence-transformers/all-roberta-large-v1')
#embeddings = model.encode(sentences)
#print(embeddings)

@app.route('/sentences2embeddings', methods=["POST"])
def sentences2embeddings():
    data = request.get_json()
    sentences = data.get('sentences', [])

    embeddings = model.encode(sentences)
    embeddings = embeddings.tolist()
    app.logger.info(type(embeddings))
    #return jsonify(embeddings=embeddings)
    return embeddings

if __name__ == '__main__':
    app.run(port=5001, debug=True)
