# 📧 Mass Email Job Application Automation

This project is a Python automation script for sending personalized job applications in bulk via email. It supports both Gmail and Outlook using secure environment variables for credentials and message content.

---

## ✅ Features
- Sends custom email to each contact in a CSV list
- Attaches your resume to every email
- Uses `.env` file for secure configuration
- Works with Gmail or Outlook via SMTP

---

## 📁 Project Files
```
MassApplicationJob/
├── emails.csv                      # Contact list (name,email,company)
├── .env                            # Environment variables
├── mass_application.py             # Main Python script
└── README.md                       # This file
```

---

## 🛠️ .env File Example
```env
PROVIDER=gmail
EMAIL=shaheedabdillah@gmail.com
PASSWORD=your_app_password_here
SUBJECT=Application – Software Dev / Tech Support / DevOps / Infra Role
RESUME_PATH=Shaheed_Abdillah_Professional_Resume.pdf
BODY_TEMPLATE=Hi {name},\n\nI'm Shaheed, an IT Support, Software Developer and Automation Engineer with 3.5 years of experience in Linux, Java, Python scripting, and backend support operations.\n\nI've worked on automating reporting systems and supporting large-scale production environments. I'm actively upskilling in AWS, Docker, and DevOps tools.\n\nPlease find my resume attached. I'd be grateful for any opportunity to contribute to {company} or if you could forward this to the relevant team.\n\nWarm regards,\nShaheed Abdillah
```

---

## 📑 CSV Format Example
```csv
name,email,company
HR Team,hr@example.com,Example Corp
Tech Lead,techlead@startup.com,Startup Inc
```

---

## 🚀 How to Use
1. Install required packages:
```bash
pip install pandas python-dotenv
```
2. Prepare your `.env` file and `emails.csv`
3. Place your resume in the same folder and match the filename in `.env`
4. Run the script:
```bash
python mass_application.py
```

---

## 🔐 Notes
- Do **not** commit your `.env` file to any public repo
- Always use App Passwords for Gmail and Outlook
- Ensure all required files are in the same directory

---

## 👤 Author
**Shaheed Abdillah**  
shaheedabdillah@gmail.com  
Singapore

---

Automate the grind. Apply smarter. Get hired.
