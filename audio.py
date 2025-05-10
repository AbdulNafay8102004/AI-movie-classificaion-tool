import pandas as pd
from gtts import gTTS
import os
import re

# Load translated CSV
df = pd.read_csv("translated_data.csv")

# Define language columns and corresponding gTTS language codes
language_map = {
    'summary_arabic': 'ar',
    'summary_urdu': 'ur',
    'summary_spanish': 'es'
}

output_dir = "audio_summaries"
os.makedirs(output_dir, exist_ok=True)

# Function to sanitize filenames
def safe_filename(text):
    return re.sub(r'[\\/*?:"<>|]', "", text)

# Generate audio
for idx, row in df.iterrows():
    for col, lang_code in language_map.items():
        text = str(row[col]).strip()
        if not text or len(text) < 5:
            print(f"⚠ Skipping short/empty summary at index {idx} for {col}")
            continue
        try:
            tts = gTTS(text=text, lang=lang_code)
            filename = f"{output_dir}/{safe_filename(str(idx))}_{lang_code}.mp3"
            tts.save(filename)
            print(f"✅ Saved: {filename}")
        except Exception as e:
            print(f"❌ Error at index {idx} for {col}: {e}")
