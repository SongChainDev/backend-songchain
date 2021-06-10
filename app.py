from flask import Flask, request
import requests

xooa = "https://api.xooa.com/api/v2/"
app = Flask(__name__)

@app.route("/ping", methods=["POST"])
def listen_ping():
    name = request.form.get("name")
    return f"Hello {name}!\n"

@app.route("/authenticate", methods=["POST"])
def listen_authenticate():
    tok = request.form.get("token")
    r = requests.get(xooa + "identities/me", headers={"Authorization": "Bearer " + tok})
    name = r.json()["IdentityName"]
    return f"Hello {name}!\n"

if __name__ == "__main__":
    app.run()
