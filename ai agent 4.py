from anthropic import Anthropic
import replicate
import os
import subprocess  # Use for playing audio in Windows

# Load API keys from environment variables
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

if not ANTHROPIC_API_KEY:
    raise ValueError("Anthropic API key is missing. Set it as an environment variable.")
if not REPLICATE_API_TOKEN:
    raise ValueError("Replicate API token is missing. Set it as an environment variable.")

# Initialize the Anthropic client
client = Anthropic(api_key=ANTHROPIC_API_KEY)

SYSTEM_PROMPT = """
You are the smartest doctor to have ever lived, smarter than Einstein. 
You are the Einstein of the medical field.
You are a female character with a soft demeanor.
You speak with confidence and assure the person you can heal them.
You graduated from the Stanford School of Medicine.
"""

def chat():
    """Chat loop to interact with the AI."""
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat...")
            break

        # Create a message using Claude's API
        response = client.messages.create(
            model="claude-3-sonnet-20240229",  # Change if needed
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_input}]
        )

        answer = response.content[0].text
        print("\nAI:", answer)

        try:
            say(answer)
        except Exception as e:
            print(f"Text-to-speech error: {e}")
            print("Continuing with text-only response...")

def say(text):
    """Convert text to speech using Replicate API and play the audio."""
    try:
        output = replicate.run(
            "jaaari/kokoro-82m:f559560eb822dc509045f3921a1921234918b91739db4bf3daab2169b71c7a13",
            input={"text": text, "speed": 1.1, "voice": "af_nicole"}
        )

        output_file = "output.wav"
        with open(output_file, "wb") as file:
            for chunk in output:  # Correctly handle the generator output
                file.write(chunk)

        # Play the sound using subprocess (ffplay required)
        subprocess.run(["ffplay", "-nodisp", "-autoexit", output_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Clean up the audio file
        os.remove(output_file)

    except Exception as e:
        print(f"Error generating speech: {e}")

if __name__ == "__main__":
    chat()
