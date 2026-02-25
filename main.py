import argparse
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("GEMINI_API_KEY environment variable not set")

client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser(description="Chatbot for Boot.dev")
parser.add_argument("user_prompt", type=str, default="gemini-2.5-flash", help="User prompt to send to the chatbot")
args = parser.parse_args()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=args.user_prompt
)
if response.usage_metadata is None:
    raise RuntimeError("Usage metadata is not available in the response")

print("Prompt tokens:", response.usage_metadata.prompt_token_count)
print("Response tokens:", response.usage_metadata.candidates_token_count)
print("Response:")
print(response.text)