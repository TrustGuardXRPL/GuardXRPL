
from flask import Flask, render_template, request, redirect
from xrpl.clients import JsonRpcClient
from xrpl.models.requests import AccountLines

app = Flask(__name__)
client = JsonRpcClient("https://s1.ripple.com:51234")

# Статические данные (можно заменить на базу)
reports = []

@app.route("/")
def index():
    return render_template("index.html", reports=reports)

@app.route("/check", methods=["POST"])
def check_token():
    account = request.form["issuer"]
    try:
        req = AccountLines(account=account)
        response = client.request(req)
        lines = response.result.get("lines", [])
        return render_template("result.html", lines=lines, account=account)
    except Exception as e:
        return f"Error: {e}"

@app.route("/report", methods=["POST"])
def report_token():
    token = request.form["token"]
    reason = request.form["reason"]
    reports.append({"token": token, "reason": reason})
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
