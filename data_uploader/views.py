import os
import fitz  # PyMuPDF
import pickle
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from sentence_transformers import SentenceTransformer
import faiss

# Function to extract text from PDF file path
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to split text into chunks
def chunk_text(text, chunk_size=500, overlap=50):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def upload_file(request):
    message = ''
    if request.method == 'POST' and request.FILES.get('pdf'):
        pdf = request.FILES['pdf']
        fs = FileSystemStorage()
        filename = fs.save(pdf.name, pdf)
        message = f'File {filename} uploaded successfully.'
    return render(request, 'data_uploader/upload.html', {'message': message})

def build_faiss_index(request):
    message = ''
    # Location where PDFs are stored
    media_dir = settings.MEDIA_ROOT
    pdf_files = [os.path.join(media_dir, f) for f in os.listdir(media_dir) if f.endswith('.pdf')]
    
    if not pdf_files:
        message = "No PDF files found in media folder to process."
        return render(request, 'data_uploader/upload.html', {'message': message})
    
    all_texts = []
    for pdf_file in pdf_files:
        text = extract_text_from_pdf(pdf_file)
        all_texts.append(text)
    
    # Combine all text
    combined_text = "\n".join(all_texts)
    
    # Chunk text
    chunks = chunk_text(combined_text)
    
    # Load embedding model (you can pick another if you want)
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Create embeddings
    embeddings = model.encode(chunks)
    
    # Build FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    
    # Save index and documents
    os.makedirs(os.path.join(settings.BASE_DIR, 'models_store'), exist_ok=True)
    faiss.write_index(index, os.path.join(settings.BASE_DIR, 'models_store', 'faiss_index.pkl'))
    with open(os.path.join(settings.BASE_DIR, 'models_store', 'documents.pkl'), 'wb') as f:
        pickle.dump(chunks, f)
    
    message = f"FAISS index built and saved with {len(chunks)} text chunks."
    return render(request, 'data_uploader/upload.html', {'message': message})

