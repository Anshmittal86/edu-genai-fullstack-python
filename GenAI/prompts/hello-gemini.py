from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model='gemini-3-flash-preview',
    messages=[
        { 'role': 'system', 'content': 'You are helpful AI Assistant.' },
        { 'role': 'user', 'content': 'Hello How are You?' }
    ]
)

print(response.choices[0].message.content)