from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('user_input')

    client = OpenAI(
        api_key="sk-c97ddcecdb034abf93eba386d3f7100c",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    completion = client.chat.completions.create(
        model="qwen-omni-turbo",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ],
        modalities=["text", "audio"],
        stream=True
    )

    full_response = ""
    for chunk in completion:
        if 'audio' in chunk.choices[0].delta and 'transcript' in chunk.choices[0].delta.audio:
            full_response += chunk.choices[0].delta.audio['transcript']

    return jsonify({'response': full_response})


if __name__ == '__main__':
    app.run(debug=True)