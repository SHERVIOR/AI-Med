# AI-Med


This project is a voice-enabled AI medical assistant that uses **Anthropic Claude** for intelligent text-based responses and **Replicate TTS** for generating spoken audio replies. It creates an interactive, voice-based conversational experience tailored for general health inquiries, with a fictional character designed to emulate a calm and knowledgeable doctor.

---

## Features

- Accepts user input via keyboard (can be extended to speech)
- Uses Claude (Anthropic) for advanced medical dialogue and context understanding
- Converts Claude's response into natural-sounding voice using Replicate’s TTS models
- Plays the response out loud using `ffplay` on Windows (or other platforms)

---

## AI Doctor Character

- Persona: A kind, confident, Stanford-educated female doctor
- Behavior: Reassuring, intelligent, and conversational
- Powered by: `claude-3-sonnet-20240229`

---

## Setup Instructions

### Prerequisites

- Python 3.8+
- `ffmpeg` installed and available in system PATH (for `ffplay`)
