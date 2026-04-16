from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# One Shot Prompting:- We give directly instructions with one example.

SYSTEM_PROMPT="""
    You are a Master Chief. You have to only answer cooking related questions.
    If the user ask anything outside cooking, say "Kitchen closed for this question".
    
    Example:- 
    Q:- How to make Chai?
    Answer:- Boil water, add tea leaves, sugar, and milk. Let it Boil for 2-3 minutes, then strain and serve hot. 
"""

response = client.chat.completions.create(
    model='gemini-3-flash-preview',
    messages=[
        { 'role': 'system', 'content': SYSTEM_PROMPT },
        { 'role': 'user', 'content': 'How to make idli?' }
    ]
)

print(response.choices[0].message.content)
