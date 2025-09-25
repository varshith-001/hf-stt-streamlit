# 🎙️ Speech → Text (Streamlit + faster-whisper)

[![Streamlit](https://img.shields.io/badge/Streamlit-1.36+-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)  
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-faster--whisper-yellow?logo=huggingface&logoColor=white)](https://huggingface.co/)  

A simple **speech-to-text web app** built with [Streamlit](https://streamlit.io/) and [faster-whisper](https://github.com/guillaumekln/faster-whisper).  
This project is **just an experiment** to learn Git, Python, and deployment basics — but it shows how powerful Whisper models can be.  
🚧 A lot more can be done with this app in the future!

---

## ✨ Features
- Upload audio (`.wav`, `.mp3`, `.m4a`, `.flac`, `.ogg`, `.webm`)
- Choose model size (`tiny` → `large-v3`)
- Auto language detection, with optional manual language hint
- Translate speech directly to English
- Download transcripts as `.txt`

---
## ⚡ Quick Start

### macOS
```bash
git clone https://github.com/varshith-001/hf-stt-streamlit.git
cd hf-stt-streamlit

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
brew install ffmpeg

python -m streamlit run app.py

###  Windows
git clone https://github.com/varshith-001/hf-stt-streamlit.git
cd hf-stt-streamlit

py -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
# install FFmpeg (e.g. choco install ffmpeg) and add to PATH

python -m streamlit run app.py


hf-stt-streamlit/
│── app.py            # main Streamlit app
│── requirements.txt  # Python dependencies
│── README.md         # project description
│── .gitignore        # files ignored by Git
│── models/           # cached Whisper models (not committed)
│── .venv/            # virtual environment (not committed)


🔮 Future Ideas
This is only a starting point. Possible improvements:
🎤 Record audio directly in the browser (via streamlit-webrtc)
📂 Batch transcription of multiple files
🌐 Deploy online (Streamlit Cloud, Hugging Face Spaces, or Docker)
⚡ GPU acceleration for faster performance
✨ Better UI/UX (progress bars, editable transcript, subtitles)


⚠️ Disclaimer
This project is for learning and experimentation only.
It is not production-ready. Whisper models are powerful but require careful handling for accuracy, scaling, and deployment.





---

MIT License — feel free to fork and experiment further.
