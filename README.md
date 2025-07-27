# 🎙️ VoiceGPT – Lokal Türkçe Sesli Asistan

VoiceGPT, mikrofonla konuştuğunuzda sesinizi yazıya çeviren, anlamlı cevaplar üreten ve cevabı sesli olarak size okuyan tamamen **lokal çalışan** bir yapay zeka asistanıdır.

---

## 🚀 Özellikler

- Mikrofondan ses alma
- OpenAI Whisper ile ses → yazı dönüşümü
- Ollama destekli LLM (llama3) ile doğal Türkçe yanıtlar
- gTTS ile metni sese dönüştürme
- İnternetsiz çalışabilir (tamamen lokal)
- Gradio arayüzü üzerinden kullanım

---

## Kurulum

### 1. Gerekli programlar

- ✅ [Python 3.10+](https://www.python.org/downloads/)
- ✅ [FFmpeg](https://ffmpeg.org/download.html) (Whisper için zorunlu)
- ✅ [Ollama](https://ollama.com/download) (yerel LLM çalıştırmak için)

> 💡 `ollama` kurulduktan sonra terminale şu komutu girerek model indirilmelidir:

```bash
ollama run llama3
```

### 2. Proje Dosyasını ve Gereksinimleri Yükle

```bash
pip install -r requirements.txt
```

### 3. Kullanım

```bash
python app.py
```

Arayüz otomatik olarak açılır:
📍 http://127.0.0.1:7860
Mikrofona konuş.
Sesin yazıya çevrilsin.
LLM yanıt versin.
Cevap sesli olarak oynatılsın.


---
## 4. Proje Yapısı 
```
VoiceGPT/
├── app.py              # Ana Python uygulaması
├── requirements.txt    # Bağımlılıklar
├── .gradio/flagged/    # Flag edilen örnekler ve CSV
└── README.md           
```

📌 Notlar
whisper modeli base olarak yüklüdür (daha hızlı için "tiny", daha kaliteli için "small" da kullanılabilir).

Ollama ile llama3 modeli kullanılmıştır. Dilersen mistral, gemma veya llama2 ile değiştirebilirsin.

flag butonu ile ses, yanıt ve sesli çıktı .csv olarak kaydedilir (proje klasöründeki .gradio/flagged/ içinde).

Türkçe karakter desteği için gtts kullanılmıştır (doğal ve hızlı seslendirme için idealdir).

---

## 5. Ekran Görüntüleri
