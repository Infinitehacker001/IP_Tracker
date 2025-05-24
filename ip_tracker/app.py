from flask import Flask, request, render_template
import requests
import re
import nmap as np
app = Flask(__name__)

def is_valid_ip_or_domain(value):
    ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
    domain_pattern = r"^([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
    return re.match(ip_pattern, value) or re.match(domain_pattern, value)

@app.route("/", methods=["GET", "POST"])
def index():
    ip_data = None
    error = None

    if request.method == "POST":
        ip = request.form.get("ip")

        if not ip:
            ip = request.remote_addr

        if not is_valid_ip_or_domain(ip):
            error = "❌ Invalid IP or domain."
        else:
            try:
                response = requests.get(f"http://ip-api.com/json/{ip}")
                data = response.json()

                if data.get("status") == "success":
                    ip_data = data
                else:
                    error = "⚠️ Could not fetch data. Try a different IP."
            except Exception as e:
                error = f"🚫 Error: {str(e)}"

    return render_template("index.html", ip_data=ip_data or {}, error=error)

if __name__ == "__main__":
    app.run(debug=True)

