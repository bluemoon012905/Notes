from datetime import datetime
from pathlib import Path
from threading import Lock
import json

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR.parent / "static"
MESSAGES_FILE = BASE_DIR / "messages.json"
HISTORY_FILE = BASE_DIR / "history.json"

app = Flask(__name__, static_folder=str(STATIC_DIR), static_url_path="")
CORS(app)
file_lock = Lock()


def _load_json_array(file_path):
    if not file_path.exists():
        return []
    try:
        with file_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        return []


def _save_json_array(file_path, data):
    with file_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def _clean_text(value):
    return value.strip() if isinstance(value, str) else ""


@app.route("/")
def index():
    return send_from_directory(STATIC_DIR, "index.html")

@app.route("/sendMsg", methods=["POST"])
def send_msg():
    data = request.get_json(silent=True) or {}
    sender_id = _clean_text(data.get("senderID"))
    receiver_id = _clean_text(data.get("receiverID"))
    msg_content = _clean_text(data.get("msg"))

    if not sender_id or not receiver_id or not msg_content:
        return jsonify({"error": "Missing parameters"}), 400

    new_msg = {
        "senderID": sender_id,
        "receiverID": receiver_id,
        "msg": msg_content,
        "timestamp": datetime.now().isoformat(),
        "received": False,
    }

    with file_lock:
        messages = _load_json_array(MESSAGES_FILE)
        messages.append(new_msg)
        _save_json_array(MESSAGES_FILE, messages)

    return jsonify({"status": "success"}), 200


@app.route("/receiveMsg", methods=["GET"])
def receive_msg():
    receiver_id = _clean_text(request.args.get("receiverID"))
    purge = request.args.get("purge", "false").lower() == "true"

    if not receiver_id:
        return jsonify({"error": "Missing receiverID"}), 400

    with file_lock:
        messages = _load_json_array(MESSAGES_FILE)

        # Return only required fields for this assignment: sender, time, message.
        new_messages = [
            {"senderID": m.get("senderID"), "timestamp": m.get("timestamp"), "msg": m.get("msg")}
            for m in messages
            if m.get("receiverID") == receiver_id and not m.get("received", False)
        ]

        for m in messages:
            if m.get("receiverID") == receiver_id and not m.get("received", False):
                m["received"] = True

        if purge:
            messages = [m for m in messages if m.get("receiverID") != receiver_id]

        _save_json_array(MESSAGES_FILE, messages)

    return jsonify(new_messages), 200


@app.route("/saveVision", methods=["POST"])
def save_vision():
    data = request.get_json(silent=True) or {}
    topic = _clean_text(data.get("topic"))
    vision_data = data.get("vision")

    if not topic or vision_data is None:
        return jsonify({"error": "Missing data"}), 400

    with file_lock:
        history = _load_json_array(HISTORY_FILE)
        history.append({
            "topic": topic,
            "vision": vision_data,
            "timestamp": datetime.now().isoformat(),
        })
        _save_json_array(HISTORY_FILE, history)

    return jsonify({"status": "success"}), 200


@app.route("/getHistory", methods=["GET"])
def get_history():
    with file_lock:
        return jsonify(_load_json_array(HISTORY_FILE)), 200


if __name__ == "__main__":
    with file_lock:
        if not MESSAGES_FILE.exists():
            _save_json_array(MESSAGES_FILE, [])
    app.run(port=5000, debug=False)
