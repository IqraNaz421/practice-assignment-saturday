# 💼 Career Mentor Agent (Chainlit Version)

This is a Chainlit-based interactive agent that guides students through career exploration.

## Features
- ✅ Recommends career fields (Software Engineering, Data Science)
- ✅ Provides skill-building roadmaps
- ✅ Suggests real-world job roles

## Tech Used
- [Chainlit](https://www.chainlit.io/) for UI
- dotenv for OpenAI key loading

## Setup Instructions

### 1. Install dependencies
```bash
pip install chainlit python-dotenv
```

### 2. Set your API Key
Edit `.env` file:
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

### 3. Run the App
```bash
chainlit run main.py
```

Then open the link it gives you (usually http://localhost:8000) in your browser.

## Example Prompts
- `career help`
- `Software Engineering`
- `Data Science`
