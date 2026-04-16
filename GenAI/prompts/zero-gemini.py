from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Zero Shot Prompting:- We give directly instructions.

SYSTEM_PROMPT="""
    You are a Master Chief. You have to only answer cooking related questions.
    If the user ask anything outside cooking, say "Kitchen closed for this question".
"""

response = client.chat.completions.create(
    model='gemini-3-flash-preview',
    messages=[
        { 'role': 'system', 'content': SYSTEM_PROMPT },
        { 'role': 'user', 'content': 'How to make chai?' }
    ]
)

print(response.choices[0].message.content)