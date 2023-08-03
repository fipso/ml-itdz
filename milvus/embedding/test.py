from sentence_transformers import SentenceTransformer
import torch

device = "cuda:0" if torch.cuda.is_available() else "cpu"
print(device)
#device = "cpu"

s = "this is an example sentence that is longer as the ones before and should test if the gpu usage is an advantage on embedding over using cpu"
sentences = [s for _ in range(10000)]

model = SentenceTransformer("sentence-transformers/roberta-large-nli-stsb-mean-tokens")
model = model.to(device)
embeddings = model.encode(sentences)
print(embeddings.shape)
