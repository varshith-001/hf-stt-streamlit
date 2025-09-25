import os
import tempfile
import streamlit as st
from faster_whisper import WhisperModel


st.set_page_config(
    page_title="Speech → Text (Hugging Face Whisper)", page_icon="🎙️", layout="centered"
)
st.title("🎙️ Speech → Text (Hugging Face Whisper)")
st.caption("Free, local transcription using faster-whisper (no fine-tuning).")

# ── Sidebar options ────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("Settings")
    model_size = st.selectbox(
        "Model", ["tiny", "base", "small", "medium", "large-v3"], index=2
    )
    translate = st.checkbox("Translate to English", value=False)
    lang_hint = st.text_input(
        "Language hint (e.g. en, hi, fr). Leave blank for auto-detect."
    )
    vad = st.checkbox("Voice activity detection (recommended)", value=True)
    beam_size = st.slider("Beam size (quality vs speed)", 1, 8, 5)
    compute_type = st.selectbox(
        "Precision", ["auto", "int8", "int8_float16", "float16", "float32"], index=0
    )

# Cache models in a local folder so the project can be zipped and shared offline
MODEL_DIR = os.path.join(os.path.dirname(__file__), "models")
os.makedirs(MODEL_DIR, exist_ok=True)


@st.cache_resource(show_spinner=False)
def load_model(size: str, compute: str):
    # Uses GPU automatically on supported NVIDIA setups.
    # Falls back to CPU on systems without a compatible GPU.
    return WhisperModel(
        size,
        device="auto",
        compute_type=(compute if compute != "auto" else "auto"),
        download_root=MODEL_DIR,
    )


model = load_model(model_size, compute_type)

st.subheader("1) Upload audio")
audio = st.file_uploader(
    "WAV / MP3 / M4A / FLAC / OGG / WEBM",
    type=["wav", "mp3", "m4a", "flac", "ogg", "webm"],
)

if audio:
    st.audio(audio)
    if st.button("Transcribe", type="primary"):
        suffix = os.path.splitext(audio.name)[1] or ".wav"
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
            tmp.write(audio.read())
            tmp_path = tmp.name

        st.subheader("2) Transcript")
        with st.spinner("Transcribing…"):
            segments, info = model.transcribe(
                tmp_path,
                vad_filter=vad,
                beam_size=beam_size,
                language=lang_hint.strip() or None,
                task="translate" if translate else "transcribe",
            )

        full_lines = []
        for seg in segments:
            st.markdown(f"**[{seg.start:.2f}s → {seg.end:.2f}s]** {seg.text}")
            full_lines.append(seg.text)

        if full_lines:
            text_out = "\n".join(full_lines).strip()
            st.download_button(
                "Download transcript (.txt)", data=text_out, file_name="transcript.txt"
            )
        else:
            st.warning("No speech detected.")

        # cleanup
        try:
            os.remove(tmp_path)
        except Exception:
            pass
else:
    st.info("Upload an audio file to begin.")
