from flask import Flask, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

MESSAGES_FILE = 'messages.json'

def load_messages():
    if os.path.exists(MESSAGES_FILE):
        with open(MESSAGES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_messages(messages):
    with open(MESSAGES_FILE, 'w') as f:
        json.dump(messages, f, indent=4)

@app.route('/sendMsg', methods=['POST'])
def send_msg():
    data = request.json
    sender_id = data.get('senderID')
    receiver_id = data.get('receiverID')
    msg_content = data.get('msg')
    
    if not all([sender_id, receiver_id, msg_content]):
        return jsonify({"error": "Missing parameters"}), 400
    
    messages = load_messages()
    new_msg = {
        "senderID": sender_id,
        "receiverID": receiver_id,
        "msg": msg_content,
        "timestamp": datetime.now().isoformat(),
        "received": False
    }
    messages.append(new_msg)
    save_messages(messages)
    
    return jsonify({"status": "success"}), 200

@app.route('/receiveMsg', methods=['GET'])
def receive_msg():
    receiver_id = request.args.get('receiverID')
    purge = request.args.get('purge', 'false').lower() == 'true'
    
    if not receiver_id:
        return jsonify({"error": "Missing receiverID"}), 400
    
    messages = load_messages()
    
    # Filter for new messages for this receiver
    new_messages = [m for m in messages if m['receiverID'] == receiver_id and not m['received']]
    
    # Mark as received
    for m in messages:
        if m['receiverID'] == receiver_id:
            m['received'] = True
            
    if purge:
        # Remove all messages for this receiver
        messages = [m for m in messages if m['receiverID'] != receiver_id]
    
    save_messages(messages)
    
    return jsonify(new_messages), 200

@app.route('/saveVision', methods=['POST'])
def save_vision():
    data = request.json
    topic = data.get('topic')
    vision_data = data.get('vision')
    
    if not topic or not vision_data:
        return jsonify({"error": "Missing data"}), 400
    
    history_file = 'history.json'
    history = []
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history = json.load(f)
            
    history.append({
        "topic": topic,
        "vision": vision_data,
        "timestamp": datetime.now().isoformat()
    })
    
    with open(history_file, 'w') as f:
        json.dump(history, f, indent=4)
        
    return jsonify({"status": "success"}), 200

@app.route('/getHistory', methods=['GET'])
def get_history():
    history_file = 'history.json'
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            return jsonify(json.load(f)), 200
    return jsonify([]), 200

if __name__ == '__main__':
    # Initialize file if not exists
    if not os.path.exists(MESSAGES_FILE):
        save_messages([])
    app.run(port=5000, debug=True)
