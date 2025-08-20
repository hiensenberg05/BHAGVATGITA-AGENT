import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText

# Load .env variables
load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
FROM_EMAIL = os.getenv("FROM_EMAIL")
TO_EMAIL = os.getenv("TO_EMAIL")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 465))

def send_test_email():
    body = "Hello 👋\n\nThis is a test email from your Daily Gita Agent setup."
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = "✅ SMTP Test - Daily Gita Agent"
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(FROM_EMAIL, [TO_EMAIL], msg.as_string())
        print("✅ Test email sent successfully!")
    except Exception as e:
        print("❌ Failed to send test email:", e)

if __name__ == "__main__":
    send_test_email()
