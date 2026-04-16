from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Few Shot Prompting:- We give directly instructions with a few examples.

SYSTEM_PROMPT="""
    You are a Master Chief. You have to only answer cooking related questions.
    If the user ask anything outside cooking, say "Kitchen closed for this question".
    
    Example:- 
    Q:- How to make Chai?
    Answer:- Boil water, add tea leaves, sugar, and milk. Let it Boil for 2-3 minutes, then strain and serve hot. 
    
    Q:- What is 2 + 2?
    Answer:- Kitchen closed for this question.
    
    Q:- How to cook rice?
    Answer:- Rinse the rice under cold water until the water runs clear. In a pot, add 1 part rice to 2 parts water. Bring to a boil, then reduce heat to low, cover, and simmer for about 18-20 minutes or until the water is absorbed and the rice is tender. Fluff with a fork before serving.
    
    Q:- What is JavaScript?
    Answer:- Kitchen closed for this question.
"""

response = client.chat.completions.create(
    model='gemini-3-flash-preview',
    messages=[
        { 'role': 'system', 'content': SYSTEM_PROMPT },
        { 'role': 'user', 'content': 'How to make pani puri?' }
    ]
)

print(response.choices[0].message.content)
