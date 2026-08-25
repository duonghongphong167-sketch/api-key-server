from flask import Flask, request, jsonify
import secrets

app = Flask(__name__)

API_KEYS = set()

@app.get("/")
def home():
    return "API Key Server is running!"

@app.get("/generate")
def generate():
    key = "sk_" + secrets.token_urlsafe(24)
    API_KEYS.add(key)
    return jsonify({"api_key": key})

@app.get("/verify")
def verify():
    key = request.args.get("key")

    if key in API_KEYS:
        return jsonify({"valid": True})

    return jsonify({"valid": False}), 401
