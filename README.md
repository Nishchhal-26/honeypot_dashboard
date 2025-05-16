🛡️ Honeypot Deployment Dashboard

A real-time web-based dashboard to monitor and visualize cyberattacks using data from a honeypot (like Cowrie).
Built with Python, Flask, Chart.js, and IPinfo API for geolocation, this project provides an email alert system, IP tracking, and country-wise analysis of attackers.



🚀 Features
  
  1. Real-time parsing of honeypot logs

  2. Geo-IP tracking using IPinfo API

  3. Email alerts on new attacker IPs
  
  4. Visual dashboard with charts (Top IPs & Country distribution)

  5. Log viewer to inspect raw entries

  6. Lightweight and easy to deploy



🎯 Use Case

This project is ideal for:

  1. Students learning ethical hacking and cybersecurity

  2. Researchers testing honeypot deployments

  3. Anyone curious about how attackers behave

  4. Security awareness demos for organizations



🧰 Tech Stack

  Component	Technology
  
  Backend	Python + Flask
  
  Frontend	HTML + Bootstrap + Chart.js

  Email Alerts	Flask-Mail (Gmail SMTP)
  
  Geo IP Lookup	IPinfo API
  
  Logs Input	Honeypot logs (cowrie.log JSON)




![image](https://github.com/user-attachments/assets/99f71b48-9443-40d3-a453-ff5f7d73f654)




⚙️ How to Run
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/yourusername/honeypot-dashboard.git
cd honeypot-dashboard



2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt



3. Set Up .env File
Create a .env file with your email and IPinfo key:

env
Copy
Edit
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_gmail_app_password
MAIL_RECEIVER=receiver_email@gmail.com
IPINFO_API_KEY=your_ipinfo_key



4. Run the App
bash
Copy
Edit
python run.py



![WhatsApp Image 2025-05-17 at 01 25 05_4881d1db](https://github.com/user-attachments/assets/cc5f9f7b-87c7-439b-a9ed-147b9fb4b6ea)





![WhatsApp Image 2025-05-17 at 01 25 22_ff615173](https://github.com/user-attachments/assets/472fb4d6-64e5-4bb4-961c-a3ec92e4f0a0)

