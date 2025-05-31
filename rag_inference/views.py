import os
import pickle
import faiss
from django.shortcuts import render
from django.conf import settings
import json
import subprocess
from sentence_transformers import SentenceTransformer

# Define paths relative to your Django BASE_DIR
BASE_DIR = settings.BASE_DIR
INDEX_PATH = os.path.join(BASE_DIR, 'models_store', 'faiss_index.bin')
DOCS_PATH = os.path.join(BASE_DIR, 'models_store', 'documents.pkl')

# Load FAISS index and documents once, when server starts
faiss_index = faiss.read_index(INDEX_PATH)
with open(DOCS_PATH, 'rb') as f:
    documents = pickle.load(f)

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_answer(question, context_chunks):
    context = "\n\n".join([chunk[1] for chunk in context_chunks])
    prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"

    result = subprocess.run(
        ['ollama', 'run', 'llama2', prompt],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("Ollama CLI error:", result.stderr)
        return "Error generating answer."

    answer = result.stdout.strip()
    return answer


def query_rag(request):
    answer = None
    if request.method == 'POST':
        question = request.POST.get('question')
        if question:
            q_embedding = embedding_model.encode([question]).astype('float32')
            k = 5
            distances, indices = faiss_index.search(q_embedding, k)
            retrieved_chunks = [documents[idx] for idx in indices[0]]

            print("Top retrieved chunks:")
            for i, chunk in enumerate(retrieved_chunks, 1):
                print(f"{i}. {chunk[1][:200]}...")  # print first 200 chars

            answer = generate_answer(question, retrieved_chunks)

    return render(request, 'rag_inference/query.html', {'answer': answer})


    
