import requests
API_URL = "https://api-inference.huggingface.co/models/gpt2"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
data = query("Can you please let us know more details about your ")
print(data)