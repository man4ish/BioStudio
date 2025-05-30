from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from transformers import pipeline
import pandas as pd
import io

# Load Hugging Face model once when the server starts
qa_model = pipeline("text2text-generation", model="google/flan-t5-large")

def summarize_expression_csv(file):
    try:
        df = pd.read_csv(file)
        upregulated = df[(df['log2FoldChange'] > 1) & (df['padj'] < 0.05)]
        downregulated = df[(df['log2FoldChange'] < -1) & (df['padj'] < 0.05)]
        summary = (
            f"Detected {len(df)} genes. "
            f"Upregulated genes: {len(upregulated)}. "
            f"Downregulated genes: {len(downregulated)}."
        )
        return summary
    except Exception as e:
        return f"Error reading file: {str(e)}"

@csrf_exempt
def ask_question(request):
    if request.method == "POST":
        question = request.POST.get("question", "").strip()
        datafile = request.FILES.get("datafile")
        
        context = ""
        if datafile:
            context = summarize_expression_csv(datafile)
        
        if not question:
            return JsonResponse({"error": "Question is required."}, status=400)
        
        prompt = f"Context: {context}\nQuestion: {question}"
        answer = qa_model(prompt, max_length=150)[0]["generated_text"]
        
        return render(request, "bio_navigator/result.html", {"question": question, "answer": answer})
    
    return render(request, "bio_navigator/ask.html")
