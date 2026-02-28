# CSE446/598 A3 - Integration and Messaging (Spring 2026)

This folder includes:

- `Question 5.1` Messaging REST service in Python/Flask
- `Question 5.2` Web client pages (Sender and Receiver)
- Optional Antigravity-style page for Question 3

## Project Structure

- `messaging_service/app.py` - REST service (`sendMsg`, `receiveMsg`, `saveVision`, `getHistory`)
- `messaging_service/messages.json` - message buffer store
- `messaging_service/history.json` - saved Antigravity history (created at runtime)
- `static/sender.html` - sender client page
- `static/receiver.html` - receiver client page
- `static/index.html` - app landing page
- `static/antigravity_app.html` - optional Antigravity page
- `static/style.css` - shared styles

## Requirements

- Python 3.10+ (3.8+ should also work)
- Packages:
  - `flask`
  - `flask-cors`

Install:

```bash
cd /home/moonbox/school/Notes/A3
python3 -m pip install -r requirements.txt
```

## Run Instructions

Start the service:

```bash
cd /home/moonbox/school/Notes/A3/messaging_service
python3 app.py
```

Service runs on:

- `http://localhost:5000/`

The root route serves the web client UI (`static/index.html`) directly.

## Question 5 Testing Flow (Matches Assignment PDF)

Open **three browser sessions/windows**:

1. Service/UI session:
   - `http://localhost:5000/`
2. Sender session:
   - `http://localhost:5000/sender.html`
3. Receiver session:
   - `http://localhost:5000/receiver.html`

Test steps:

1. In Sender, enter `senderID`, `receiverID`, and `msg`, then click **Send Now**.
2. In Receiver, enter the same `receiverID`, optionally set purge, then click **Receive Now**.
3. Verify message appears with `senderID`, timestamp, and message content.
4. Click **Receive Now** again without sending a new message:
   - Expected: **No new messages** (old messages are not re-delivered).
5. Send another message and receive with `purge=true`:
   - Expected: message is received, then removed from storage for that receiver.

## API Summary

### `POST /sendMsg`

Input JSON:

```json
{
  "senderID": "alice",
  "receiverID": "bob",
  "msg": "hello"
}
```

Behavior:

- Saves message into `messages.json` with timestamp and unread status.

### `GET /receiveMsg?receiverID=<id>&purge=<true|false>`

Output JSON array:

- Each element contains `senderID`, `timestamp`, `msg`.
- Returns only new/unread messages for the receiver on each call.
- If `purge=true`, deletes all messages for that receiver after processing.

## Submission Notes

Per assignment instructions:

1. Include both service (`Question 5.1`) and web client (`Question 5.2`) in one folder.
2. Zip the entire solution folder.
3. Include screenshots showing end-to-end testing (service + sender + receiver sessions).
4. Ensure the project runs after unzip in a different directory/machine.
