import os
import random
import requests
from dotenv import load_dotenv

load_dotenv()

API_BASE = os.getenv("BHAGAVAD_GITA_API_BASE")  # e.g. https://bhagavad-gita3.p.rapidapi.com
API_KEY = os.getenv("BHAGAVAD_GITA_API_KEY")
API_HOST = os.getenv("BHAGAVAD_GITA_API_HOST")

def fetch_shloka(chapter, verse, language="en"):
    """Fetch a specific shloka in a given language."""
    url = f"{API_BASE}/v2/chapters/{chapter}/verses/{verse}/"
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": API_HOST
    }
    params = {"language": language}
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()

def get_random_shloka():
    """Pick a random chapter & verse, then fetch in English & Hindi."""
    # Random chapter
    chapter = random.randint(1, 18)

    # Get all verses in that chapter to know available verse numbers
    url_verses = f"{API_BASE}/v2/chapters/{chapter}/verses/"
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": API_HOST
    }
    resp_verses = requests.get(url_verses, headers=headers)
    resp_verses.raise_for_status()
    verses = resp_verses.json()

    verse_number = random.choice(verses).get("verse_number")

    # Fetch verse in English & Hindi
    en_data = fetch_shloka(chapter, verse_number, language="en")
    hi_data = fetch_shloka(chapter, verse_number, language="hi")

    return {
        "chapter": chapter,
        "verse": verse_number,
        "text": en_data.get("slok"),  # Sanskrit text
        "transliteration": en_data.get("transliteration"),
        "translation_english": en_data.get("translation"),
        "translation_hindi": hi_data.get("translation")
    }

if __name__ == "__main__":
    print(get_random_shloka())
