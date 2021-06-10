from flask import Flask, request

app = Flask(__name__)

@app.route("/ping", methods=["POST"])
def listen_ping():
    name = request.form.get("name")
    return f"Hello {name}!\n"

if __name__ == "__main__":
    app.run()
