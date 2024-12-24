from flask import Flask, request, jsonify
from utils.message_handler import send_note_messages
from utils.logger import setup_logger

app = Flask(__name__)
logger = setup_logger()

@app.route('/send_notes', methods=['POST'])
def send_notes():
    """
    ノート連続投稿APIエンドポイント
    """
    try:
        data = request.json
        user_id = data.get("user_id")
        notes = data.get("notes")
        interval = data.get("interval", 2)

        if not user_id or not notes:
            return jsonify({"success": False, "error": "user_idまたはnotesが不足しています。"}), 400

        send_note_messages(user_id, notes, interval)
        return jsonify({"success": True, "message": "ノートが正常に送信されました。"}), 200

    except Exception as e:
        logger.error(f"Error in /send_notes: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000)
