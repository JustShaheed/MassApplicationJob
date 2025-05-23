import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
import os

load_dotenv()

provider = os.getenv("PROVIDER")
your_email = os.getenv("EMAIL")
your_password = os.getenv("PASSWORD")
subject = os.getenv("SUBJECT")
resume_path = os.getenv("RESUME_PATH")

body_template = os.getenv("BODY_TEMPLATE").replace("\\n", "\n")

if provider == "gmail":
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
elif provider == "outlook":
    smtp_server = "smtp.office365.com"
    smtp_port = 587
else:
    raise ValueError("Unsupported provider. Use 'gmail' or 'outlook'.")

email_list = pd.read_csv("emails.csv")

server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(your_email, your_password)

for _, row in email_list.iterrows():
    msg = MIMEMultipart()
    msg["From"] = your_email
    msg["To"] = row["email"]
    msg["Subject"] = subject

    body = body_template.format(name=row["name"], company=row["company"])
    msg.attach(MIMEText(body, "plain"))

    with open(resume_path, "rb") as f:
        resume = MIMEApplication(f.read(), _subtype="pdf")
        resume.add_header('Content-Disposition', 'attachment', filename=os.path.basename(resume_path))
        msg.attach(resume)

    server.send_message(msg)
    print(f"Sent to {row['company']}")

server.quit()
