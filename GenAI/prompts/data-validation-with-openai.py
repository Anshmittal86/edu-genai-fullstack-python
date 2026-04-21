from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

client = OpenAI()


class MyClass(BaseModel):
    isCookingRelated: bool 
    content: str

# Few Shot Prompting:- We give directly instructions with a few examples.

SYSTEM_PROMPT="""
    You are a Master Chief. You have to only answer cooking related questions.
    If the user ask anything outside cooking, say "Kitchen closed for this question".
    
    Rules:- 
    - Strictly Follow this Output Format.
    
    {
        'isCookingRelated': True/False,
        'content': 'Your answer here'
    } 
    
    Example:- 
    Q:- How to make Chai?
    Answer:- 
    {
        'isCookingRelated': True,
        'content': 'Boil water, add tea leaves, sugar, and milk. Let it Boil for 2-3 minutes, then strain and serve hot.'
    } 
    
    Q:- What is 2 + 2?
    Answer:- 
    {
        'isCookingRelated': False,
        'content': 'Kitchen closed for this question.'
    }
    
    Q:- How to cook rice?
    Answer:- 
    {
        'isCookingRelated': True,
        'content': 'Rinse the rice under cold water until the water runs clear. In a pot, add 1 part rice to 2 parts water. Bring to a boil, then reduce heat to low, cover, and simmer for about 18-20 minutes or until the water is absorbed and the rice is tender. Fluff with a fork before serving.'
    }

    
    Q:- What is JavaScript?
    Answer:- 
    {
        'isCookingRelated': False,
        'content': 'Kitchen closed for this question.'
    }
"""

response = client.chat.completions.parse(
    model='gpt-4o-mini',
    response_format=MyClass,
    messages=[
        { 'role': 'system', 'content': SYSTEM_PROMPT },
        { 'role': 'user', 'content': 'How to make pani puri?' }
    ]
)

print(response.choices[0].message.parsed)
