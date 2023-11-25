from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/gpt2"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        question = data["question"]
        
        # 使用 Hugging Face API 进行预测
        payload = {"inputs": question}
        result = query(payload)

        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
