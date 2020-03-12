from flask import Flask, request, send_from_directory
import os, eventlet
from visualmath.core import compute
app = Flask(__name__)
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")

@app.route("/", methods=['GET', 'POST'])
def retIndex():
    return send_from_directory(root, "index.html")

@app.route("/<path:filename>", methods=['GET', 'POST'])
def ReFile(filename):
    return send_from_directory(root, filename)
@app.route("/compute", methods=['GET'])
def main():
    content = request.args.get("content")
    setting = request.args.get("setting")
    return compute(content, setting)
@app.errorhandler(404)
def errorNotFind(error):
    return send_from_directory(root, "404.html"), 404

if __name__ == "__main__":
    app.run(port = 3389)