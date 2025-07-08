import streamlit as st
import whisper
from gtts import gTTS
import os
from PIL import Image
import matplotlib.pyplot as plt

st.set_page_config(page_title="Uzhavan Saathi", layout="centered")
st.title("🌾 உழவன் சாத்தி (Uzhavan Saathi)")
st.markdown("**Voice-driven AI Assistant for Tamil Farmers**")

# Upload audio file
audio_file = st.file_uploader("🎙 Upload your voice query (Tamil) as .mp3 or .wav", type=["mp3", "wav"])

if audio_file:
    with open("input_audio.wav", "wb") as f:
        f.write(audio_file.read())

    st.success("✅ Audio uploaded. Transcribing...")

    # Transcribe using Whisper
    model = whisper.load_model("base")
    result = model.transcribe("input_audio.wav", language='ta')
    query = result["text"]

    st.write("📝 **Transcribed Text:**", query)

    # Dummy logic
    if "poochi" in query or "இலை" in query:
        st.image("data/pest.jpg", caption="🌿 Brown Plant Hopper Detected")
        st.markdown("**🧪 Fertilizer Advice:** Use Neem Spray")
        st.image("data/spray.jpg", caption="🧴 Neem Spray Recommendation")

        # Plotting mock price trend
        prices = [20, 22, 24, 27, 30]
        weeks = ["Week 1", "2", "3", "4", "5"]
        fig, ax = plt.subplots()
        ax.plot(weeks, prices, marker='o')
        ax.set_title("📈 Paddy Price Forecast (₹/kg)")
        st.pyplot(fig)

        # Tamil voice output
        response_text = "இது பவுன் பிளாண்டு ஹாப்பர். நீம் ஸ்ப்ரே பயன்படுத்தவும். விலை அதிகரிக்கலாம்."
        tts = gTTS(response_text, lang='ta')
        tts.save("audio/output_tamil.mp3")

        st.audio("audio/output_tamil.mp3")

    else:
        st.warning("⚠️ Unable to identify. Please try a different symptom.")
