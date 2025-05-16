from flask import Blueprint, render_template
from app.utils import get_country, send_alert
import json

main = Blueprint("main", __name__)

@main.route("/")
def dashboard():
    log_file = "logs/cowrie.log"
    logs = []
    ip_counts = {}
    country_hits = {}

    try:
        with open(log_file, "r") as f:
            for line in f:
                logs.append(line.strip())
                try:
                    data = json.loads(line)
                    ip = data.get("src_ip", "")
                    if ip:
                        ip_counts[ip] = ip_counts.get(ip, 0) + 1
                        send_alert(ip)
                        country = get_country(ip, "a1beb8096a67b1")  # Replace this
                        country_hits[country] = country_hits.get(country, 0) + 1
                except:
                    continue
    except Exception as e:
        print(f"Error reading log: {e}")

    top_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)
    country_data = sorted(country_hits.items(), key=lambda x: x[1], reverse=True)

    return render_template("index.html", logs=logs, top_ips=top_ips, country_data=country_data)
