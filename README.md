# Bhagavad Gita Daily Email Agent

This project sends a daily uplifting email with a verse from the Bhagavad Gita, including Sanskrit, Hindi, and English translations, a poetic explanation, and a motivational takeaway.

## Features
- Fetches a random shloka from the Bhagavad Gita using RapidAPI
- Formats the email using Google Gemini (Generative AI)
- Sends the email via SMTP
- Can be scheduled to run automatically (e.g., with GitHub Actions)

## Files
- `agent.py`: Main script to fetch, format, and send the email
- `api.py`: Handles API requests to fetch shlokas
- `requirements.txt`: Python dependencies
- `.env`: Stores sensitive environment variables (ignored by git)
- `.gitignore`: Ignores venv, __pycache__, .env, and .pyc files
- `codesnippet.js`: Example Node.js snippet for API usage

## Setup
1. Clone the repository
2. Create a `.env` file with your API keys and email credentials
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:
   ```bash
   python agent.py
   ```

## Scheduling
- Use GitHub Actions, PythonAnywhere, or Windows Task Scheduler to automate daily emails

## API Reference
- Uses [Bhagavad Gita API on RapidAPI](https://rapidapi.com/)

## License
MIT
