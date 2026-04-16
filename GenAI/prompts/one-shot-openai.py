from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# One Shot Prompting:- We give directly instructions with one example.

SYSTEM_PROMPT="""
    You are a Master Chief. You have to only answer cooking related questions.
    If the user ask anything outside cooking, say "Kitchen closed for this question".
    
    Example:- 
    Q:- How to make Chai?
    Answer:- Boil water, add tea leaves, sugar, and milk. Let it Boil for 2-3 minutes, then strain and serve hot. 
"""

response = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        { 'role': 'system', 'content': SYSTEM_PROMPT },
        { 'role': 'user', 'content': 'How to make idli?' }
    ]
)

print(response.choices[0].message.content)
