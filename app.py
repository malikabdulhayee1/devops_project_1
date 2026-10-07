from flask import Flask, request

app = Flask(__name__)

MENU = """
<h2>Flask DevOps Project 1 for Devops PortFolio</h2>
<a href="/info">info me</a> |
<a href="/mail">mail me</a> |
<a href="/me">about me</a> |
<a href="/name">tell me ur name</a> |
<a href="/health">health</a>
"""


@app.route("/")
def home():
    return MENU


@app.route("/info")
def info():
    return "this is Abduls work for Future Ready Devops Project 1"


@app.route("/mail")
def mail():
    return "this is mail v2 via Jenkins"


@app.route("/me")
def about_me():
    n = "Abdul"
    return f"i m {n}"


@app.route("/name")
def name():
    user = request.args.get("user")
    if user:
        return f"Hello {user}!"
    return """
    <p>Tell me ur name</p>
    <form action="/name">
      <input name="user" />
      <input type="submit" />
    </form>
    """


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
