import argparse
import os

from openai.types.chat import ChatCompletionMessageParam
from dotenv import load_dotenv # type: ignore
from openai import OpenAI

# Load environment variables from .env file and get the API key
load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Ensure the API key exists before proceeding
if api_key is None:
    raise RuntimeError("OPENROUTER_API_KEY environment variable not set")

# Set up argument parsing to get the user prompt from the command line
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
# Now we can access `args.user_prompt`

# Build the message content to send to the model, using the user prompt from the command line
user_prompt = args.user_prompt

messages: list[ChatCompletionMessageParam] = [
    {"role": "user", "content": user_prompt},
]

# Send the message to the model and get the response
response = client.chat.completions.create(
    model="openrouter/free", 
    messages=messages,
    temperature=0,
)

# Verify that usage metadata is available in the response before trying to access it
if response.usage is None:
    raise RuntimeError("Usage data is not available in the response")

# If verbose mode is enabled, print the user prompt and token counts from the response
# otherwise, just print the response text
if args.verbose:
    print("User prompt:", user_prompt)
    print("Prompt tokens:", response.usage.prompt_tokens)
    print("Response tokens:", response.usage.completion_tokens)
print("Response:")
print(response.choices[0].message.content)