from django.db import models

class AnnotatedFile(models.Model):
    file = models.FileField(upload_to='bioagent/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
