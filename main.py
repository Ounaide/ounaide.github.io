from flask import *
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
  return "hello world"

@app.route("/<path:p>")
def catch_all(p):
  return redirect(url_for("index"))
  
if __name__ == "__main__":
  app.run(host="0.0.0.0")
