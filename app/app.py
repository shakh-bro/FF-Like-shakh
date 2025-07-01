from flask import Flask, request, jsonify
from config import CONFIG
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Free Fire Like API ishlayapti!"

@app.route('/like')
def like_handler():
    uid = request.args.get("uid")
    region = request.args.get("region", "IND").upper()

    if not uid:
        return jsonify({"status": "error", "message": "UID kerak!"}), 400

    config_file = CONFIG.get(region)
    if not config_file:
        return jsonify({"status": "error", "message": f"{region} mavjud emas"}), 404

    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            guest_data = json.load(f)
        
        # Bu yerda sizning like yuborish funksiyangiz chaqiriladi
        # Hozircha test sifatida shunchaki JSON qaytaramiz:
        return jsonify({
            "status": "success",
            "uid": uid,
            "region": region,
            "guest_count": len(guest_data.get("guests", []))
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500