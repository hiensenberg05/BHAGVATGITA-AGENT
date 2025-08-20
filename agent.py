import os
from dotenv import load_dotenv
from api import get_random_shloka
import smtplib
from email.mime.text import MIMEText
import google.generativeai as genai

load_dotenv()

# Load ENV variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
FROM_EMAIL = os.getenv("FROM_EMAIL")
TO_EMAIL = os.getenv("TO_EMAIL")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT") or 465)
EMAIL_SUBJECT = os.getenv("EMAIL_SUBJECT", "🌞 Your Daily Gita Shloka")

# Configure Google LLM
genai.configure(api_key=GOOGLE_API_KEY)

def format_with_llm(shloka_data):
    """Ask Gemini to prepare a beautiful structured daily Gita email in a clear, readable format (no markdown or asterisks)."""
    prompt = f"""
    You are a wise and poetic spiritual writer.
    Create a structured, uplifting morning email for this Bhagavad Gita verse.
    Do not use markdown, asterisks, or bullet points. Use clear section headers and short paragraphs.

    Required Sections:
    Shloka Reference – Chapter {shloka_data['chapter']}, Verse {shloka_data['verse']}
    Sanskrit Shloka – exact Sanskrit text
    Hindi Translation – exact Hindi text
    English Translation – exact English text
    Poetic Explanation – 4–6 soulful sentences explaining the verse meaning
    Daily Takeaway – 1–2 motivational lines for the day

    Sanskrit:
    {shloka_data['text']}

    Hindi Translation:
    {shloka_data['translation_hindi']}

    English Translation:
    {shloka_data['translation_english']}
    """

    model = genai.GenerativeModel(GEMINI_MODEL)
    response = model.generate_content(prompt)
    return response.text.strip()

def send_email(body):
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = EMAIL_SUBJECT
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(FROM_EMAIL, [TO_EMAIL], msg.as_string())

def main():
    # 1. Fetch random shloka (Hindi + English)
    shloka_data = get_random_shloka()

    # 2. Format via LLM
    email_body = format_with_llm(shloka_data)

    # 3. Send via email
    send_email(email_body)
    print("✅ Email sent successfully!")

if __name__ == "__main__":
    main()
