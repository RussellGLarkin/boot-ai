import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env file and get the API key
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Ensure the API key exists before proceeding
if api_key is None:
    raise RuntimeError("GEMINI_API_KEY environment variable not set")

# Initialize the GenAI client with the API key
client = genai.Client(api_key=api_key)

# Set up argument parsing to get the user prompt from the command line
parser = argparse.ArgumentParser(description="Chatbot for Boot.dev")
parser.add_argument("user_prompt", type=str, default="gemini-2.5-flash", help="User prompt to send to the chatbot")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

# Build the message content to send to the model, using the user prompt from the command line
messages = [
    types.Content(
        role="user",
        parts=[types.Part(text=args.user_prompt)]
    )
]

# Send the message to the model and get the response
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages
)

# Verify that usage metadata is available in the response before trying to access it
if response.usage_metadata is None:
    raise RuntimeError("Usage metadata is not available in the response")

# Print the token counts and the response text
if args.verbose:
    print("User prompt:", args.user_prompt)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
print("Response:")
print(response.text)