from django.shortcuts import render, redirect
from .forms import VCFUploadForm
from .llm_client import interpret_variants

def variant_interpreter_view(request):
    interpretation = ""
    if request.method == "POST":
        form = VCFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            vcf_file = request.FILES['vcf_file']
            vcf_text = vcf_file.read().decode('utf-8')

            prompt = form.cleaned_data['prompt']
            if not prompt.strip():
                prompt = "Interpret the following VCF variants with detailed explanation."

            # Combine user prompt with VCF data
            full_prompt = f"{prompt}\n\nHere is the VCF data:\n\n{vcf_text}"

            # Call your LLM or interpretation function
            interpretation = interpret_variants(full_prompt)
            interpretation = interpretation.replace("<think>", "").replace("</think>", "")

    else:
        form = VCFUploadForm()

    return render(request, "variant_interpreter/upload.html", {
        "form": form,
        "interpretation": interpretation,
    })
