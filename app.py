from flask import Flask
import requests

app = Flask(__name__)

def prompt(message):
    headers = {
        'Authorization': 'Bearer pk-ViEVAiyMmtSMbqxcLEaSCkRPFDwMJZdAZRsecqxayhkxfNOv',
        'Content-Type': 'application/json'
    }

    json_data = {
        'model': 'pai-001-light-beta',
        'max_tokens': 2000,
        'messages': [
            {
                'role': 'system',
                'content': 'You are an helpful assistant.',
            },
            {
                'role': 'user',
                'content': message,
            },
        ],
    }

    response = requests.post('https://api.pawan.krd/pai-001-light-beta/v1/chat/completions', headers=headers, json=json_data)
    return response.json()

@app.route('/')
def hello_world():
    return prompt("how are you?")


if __name__ == '__main__':
    app.run()