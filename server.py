from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/emotion_detector', methods=['POST'])
def emotion_detector():
    data = request.get_json()

    # 데이터가 없으면 400 에러 반환
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # 'emotion' 키가 없으면 400 에러 반환
    emotion = data.get('emotion')
    if not emotion:
        return jsonify({"error": "Emotion field is missing"}), 400

    # 정상적인 요청이라면 감정 분석 결과 반환
    return jsonify({"message": f"Emotion detected: {emotion}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
