from django.shortcuts import render, redirect
from .forms import FileUploadForm
from django.core.mail import send_mail
from django.conf import settings

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()

            # Send confirmation email
            send_mail(
                subject='BioStudio: File Uploaded',
                message='Your file has been uploaded. You may now reply to this email with your question.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[instance.email],
                fail_silently=False
            )
            return render(request, 'bioagent/upload.html', {'form': form, 'success': True})
    else:
        form = FileUploadForm()
    return render(request, 'bioagent/upload.html', {'form': form})
