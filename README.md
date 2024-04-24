# EduPersona 🎓

EduPersona is a web-based interactive chatbot that utilizes advanced AI technologies to enhance the educational experience. The application leverages OpenAI's language and speech synthesis models to provide real-time audio responses to user queries, making learning more accessible and engaging.

## Features 🌟

- **Voice-Activated Input:** Users can submit their questions through voice, which are transcribed using OpenAI's Whisper model.
- **Image Analysis:** The chatbot can analyze images uploaded by the user and generate contextual responses based on the content of the image.
- **Customizable Responses:** Users can choose the subject, tone, and grade level for the chatbot's responses, tailoring the dialogue to suit educational needs.
- **Dynamic Voice Responses:** Users can select from multiple voice options for the chatbot's audio output, including Alloy, Echo, Fable, Onyx, Nova, and Shimmer.

## Technology Stack 🛠️

- **Flask:** A lightweight WSGI web application framework used to serve the EduPersona application.
- **OpenAI API:** Used for transcribing audio, analyzing images, generating text responses, and synthesizing speech.
- **JavaScript and Bootstrap:** For the front-end user interface and interactivity.

## AI Models and APIs 🤖

- **Whisper Model:** Transcribes audio input to text.
- **GPT-4 Model:** Generates answers to user queries and provides content descriptions for images.
- **TTS (Text-to-Speech) Model:** Converts the chatbot's text responses into audio output in various selectable voices.

## Dependencies 📦

- Flask
- OpenAI
- Python packages: `os`, `base64`, `requests`
- Front-end: HTML5, Bootstrap, JavaScript

## Installation 🔧

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/EduPersona.git
cd EduPersona
```


2. **Set Up a Virtual Environment** (Optional but recommended)
```bash
-m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```


3. **Install Dependencies**
```bash
pip install Flask
pip install requests
pip install openai
```


4. **Configure API Key**
- Create a file named `config.py` in the root directory of the project.
- Add the following line to `config.py` to define your OpenAI API key:
```bash
API_KEY = 'your_openai_api_key_here'
```
- Ensure that this key matches the one you have from OpenAI and replace `your_openai_api_key_here` with your actual API key.

6. **Run the Application**
```bash
flask run
```

## Security Best Practices 🔒

- Protect API Keys: Do not commit `config.py` or any files containing sensitive information like API keys to version control systems. Ensure `config.py` is listed in your `.gitignore` file to prevent accidental exposure.

## Configuration ⚙️

- Make sure the API key in `config.py` is set correctly.
- Configure the Flask application's port and debug options as needed for your development environment.

## Usage 📚

1. **Access the Web Interface** by navigating to `http://localhost:5000` in your web browser after starting the application.
2. **Interact with the chatbot** by selecting options for subject, tone, and grade level, and using the microphone to input questions or upload images for analysis.
3. **Select a voice** from the dropdown menu for voice responses tailored to your preference.

---
Thank you for visiting the EduPersona repository!
