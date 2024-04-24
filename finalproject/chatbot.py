from flask import Flask, request, jsonify, render_template
import openai
import os
import base64
import requests

# Assuming you have a separate config.py file with your API_KEY
import config

app = Flask(__name__)
openai.api_key = config.API_KEY

@app.route("/")
def index():
    return render_template("chatbot.html")

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file"}), 400
    
    audio = request.files['audio']
    filename = "user_audio.webm"
    audio_path = os.path.join(filename)
    audio.save(audio_path)

    with open(audio_path, "rb") as file:
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=file,
            response_format="text"
        )
    print(transcript)
    # os.remove(audio_path)  # Optional: remove the file after processing

    return jsonify({"transcript": transcript}), 200

@app.route('/synthesize', methods=['POST'])
def synthesize():
    data = request.get_json()
    text = data['text']

    textResponse = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": text,
            },
        ],
    )
    answer = textResponse.choices[0].message.content
    
    voiceResponse = openai.audio.speech.create(
        model="tts-1",
        voice="nova",  # Experiment with different voices (alloy, echo, fable, onyx, nova, and shimmer) 
        input=answer
    )
    
    voiceResponse.stream_to_file("synthesized.mp3")
    
    return jsonify("Success")

@app.route('/analyze', methods=['POST'])
def analyze_image():
    subject = request.form.get('subject', '').strip('📚🧮📖🧪📜')
    tone = request.form.get('tone', '')
    gradeLevel = request.form.get('gradeLevel', '')
    question = request.form.get('question', '')
    file = request.files.get('file') if 'file' in request.files else None

    context = f"Take the persona of a(n) {subject} professor and answer this question in the tone of a {tone} as if you were talking to a {gradeLevel} student: {question}\n\n Additionally, create a 5 question worksheet."

    if file and file.filename:
        base64_image = base64.b64encode(file.read()).decode('utf-8')
        headers = {
            "Authorization": f"Bearer {openai.api_key}"
        }
        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "What's in this image?"
                        },
                        {
                            "type": "image_url",
                            "image_url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        description = response.json().get("choices")[0].get("message").get("content")
        combined_context = f"{context}\n\nBased on the image: {description}"
    else:
        combined_context = context

    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a knowledgeable professor."},
                {"role": "user", "content": combined_context},
            ],
        )
        answer = response.choices[0].message.content
    except Exception as e:
        answer = str(e)

    return jsonify(answer=answer)

if __name__ == '__main__':
    app.run(debug=True)

# https://athenarespond-bishopprague-5000.codio.io