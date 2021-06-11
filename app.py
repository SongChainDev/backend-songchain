from flask import Flask, request
import keyring
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
    if "unauthorized" in r.text:
        return "Authentication failed\n"

    name = r.json()["IdentityName"]
    keyring.set_password("backend", "apitoken", tok)
    return f"Hello {name}!\n"

@app.route("/mytokens", methods=["POST"])
def listen_mytokens():
    tok = keyring.get_password("backend", "apitoken")
    if not tok:
        return "Request failed. Please authenticate first."
    r = requests.get(xooa + "erc721/me/tokens", headers={"Authorization": "Bearer " + tok})
    return r.json()

if __name__ == "__main__":
    app.run()
