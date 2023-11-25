from flask import Flask, render_template, request, jsonify
import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

app = Flask(__name__)

# Load the pre-trained model and tokenizer
model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

@app.route('/', methods=['GET'])
def question_home():
    # Your code to process the question and context data

    # Return the HTML template
    return render_template('qa.html')

@app.route('/qa', methods=['POST'])
def question_answer():
    try:
        data = request.get_json()
        question = data['question']
        context = data['context']

        # Tokenize the input
        inputs = tokenizer(question, context, return_tensors="pt")

        # Get the answer
        with torch.no_grad():
            model_output = model(**inputs)
        
        # Get the answer
        model_output = model(**inputs)  # 调用模型获取输出

        # 提取 start_logits 和 end_logits
        start_logits = model_output.start_logits
        end_logits = model_output.end_logits
        # Find the answer span
        start_idx = torch.argmax(start_logits)
        end_idx = torch.argmax(end_logits)
        answer = tokenizer.decode(inputs['input_ids'][0][start_idx:end_idx+1])

        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)