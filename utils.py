import requests
from flask_mail import Message
from app import mail

def get_country(ip, token):
    try:
        url = f"https://ipinfo.io/{ip}?token={token}"
        r = requests.get(url)
        if r.status_code == 200:
            return r.json().get("country", "Unknown")
    except:
        pass
    return "Unknown"

def send_alert(ip):
    try:
        msg = Message(subject="Honeypot Alert!",
                      sender="your.email@gmail.com",
                      recipients=["your.email@gmail.com"],
                      body=f"New attack from IP: {ip}")
        mail.send(msg)
    except Exception as e:
        print(f"Email alert error: {e}")
