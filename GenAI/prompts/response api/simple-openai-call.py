from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model='gpt-4o-mini',
    input=[
        { 'role': 'system', 'content': 'You are helpful AI Assistant.' },
        { 'role': 'user', 'content': 'Hello How are You?' }
    ]
)

print(response.output_text)