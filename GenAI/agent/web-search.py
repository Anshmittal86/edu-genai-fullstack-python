from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5.4-nano",
    tools=[{"type": "web_search"}],
    input="What was a positive news story from today?"
)

print(response.output_text)