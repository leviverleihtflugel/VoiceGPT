# Gerekli kütüphaneleri içe aktar
import gradio as gr
import whisper
import ollama
from gtts import gTTS
import os
import tempfile

# 1. Whisper modelini yükle (local ses → metin)
model = whisper.load_model("base")  # "tiny" daha hızlı, "small"/"medium" daha kaliteli

# 2. Ollama LLM ile yanıt üret
def generate_response_with_ollama(prompt):
    # LLM'e sistem ve kullanıcı mesajı gönderilir
    response = ollama.chat(
        model="llama3",  # Alternatif: "mistral", "gemma"
        messages=[
            {
                "role": "system",
                "content": (
                    "Sen sade ve doğal Türkçe konuşan bir asistansın. "
                    "Cümlelerin düzgün ve kurallı olsun. "
                    "Yanıtlarında doğru Türkçe karakterler (ç, ğ, ı, ö, ş, ü) kullan. "
                    "Kısa ve net cevaplar ver."
                )
            },
            {
                "role": "user",
                "content": prompt  # Whisper'dan gelen metin
            }
        ]
    )
    return response["message"]["content"]

# 3. Ana işlem fonksiyonu: Ses al > Yazıya çevir > Cevapla > Sese çevir
def chat_with_voice(audio_path):
    print("⏺️ Alınan dosya yolu:", audio_path)

    # 3.1 Whisper ile ses → yazı
    try:
        result = model.transcribe(audio_path, language="tr")
        user_text = result["text"]
        print("📝 Yazıya çevrilen metin:", user_text)
    except Exception as e:
        print("❌ Whisper hatası:", repr(e))
        return f"Whisper hatası: {e}", None

    # 3.2 Ollama ile yanıt oluştur
    try:
        response_text = generate_response_with_ollama(user_text)
        print("🤖 Ollama cevabı:", response_text)
    except Exception as e:
        print("❌ Ollama hatası:", repr(e))
        return f"Ollama hatası: {e}", None

    # 3.3 gTTS ile yanıtı sese çevir
    try:
        tts = gTTS(text=response_text, lang="tr")
        tts_path = tempfile.mktemp(suffix=".mp3")
        tts.save(tts_path)
        print("🔊 Sesli yanıt kaydedildi:", tts_path)
    except Exception as e:
        print("❌ TTS hatası:", repr(e))
        return response_text, None

    return response_text, tts_path

# 4. Gradio Arayüzü
iface = gr.Interface(
    fn=chat_with_voice,
    inputs=gr.Audio(sources=["microphone"], type="filepath"),  # Mikrofon girişi
    outputs=[
        gr.Textbox(label="Yanıt"),       # Metin çıktısı
        gr.Audio(label="Sesli Yanıt")    # Ses çıktısı
    ],
    title="VoiceGPT – Lokal Whisper + Ollama Destekli Asistan",
    description="🎙️ Mikrofona konuş, yazıya çevir, Ollama modeliyle doğal cevap al ve sesli dinle!",
    allow_flagging="manual",     # Manuel flag butonu aktif
    flagging_dir="flagged",      # Flag edilen örneklerin kaydedileceği klasör
    flagging_callback=gr.CSVLogger()  # CSV formatında kaydeder
)

# 5. Uygulamayı başlat
iface.launch()
