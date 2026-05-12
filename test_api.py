import anthropic
from dotenv import load_dotenv
import os

# Load your API key from .env file
load_dotenv()
api_key = os.environ.get("ANTHROPIC_API_KEY")

# Create client
client = anthropic.Anthropic(api_key=api_key)

# Send a simple test message
response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Say hello in one sentence."}
    ]
)

# Print the response
print(response.content[0].text)