from flask import Flask, request
import json
import requests
import time

app = Flask(__name__)



@app.route('/chatgpt', methods=['POST'])
def callCHATGPT():


    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {key}"
    }

    data = request.json
    message = data["message"]
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{ "role": "user", "content": message }]
    }

    url = "https://api.openai.com/v1/chat/completions"
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        json_data = json.loads(response.text)
        response = json_data["choices"][0]["message"]["content"]
        print(response)
        return response

if __name__ == '__main__':
    app.run(port=8080)

