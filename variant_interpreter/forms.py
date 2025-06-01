from django import forms

class VCFUploadForm(forms.Form):
    vcf_file = forms.FileField(label="Upload VCF file")
    prompt = forms.CharField(
        label="Interpretation prompt",
        widget=forms.Textarea(attrs={"rows":4, "placeholder":"Type your prompt here..."}),
        required=False,
        initial="Interpret the following VCF variants with detailed explanation..."
    )
