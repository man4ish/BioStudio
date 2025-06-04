# responder.py
# This sends the AI response via email

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ollama_agent import generate_answer_from_annotation
import os

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")

# Map sender to uploaded file
# In production: use DB to look up correct file
FILE_PATH = "bioagent/uploaded/sample1.tsv"  # Example file

def send_ai_response(to_email, question):
    ai_response = generate_answer_from_annotation(FILE_PATH, question)

    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = to_email
    msg["Subject"] = "📊 BioStudio AI Answer to Your Question"

    msg.attach(MIMEText(ai_response, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        print(f"✅ Sent AI response to {to_email}")
