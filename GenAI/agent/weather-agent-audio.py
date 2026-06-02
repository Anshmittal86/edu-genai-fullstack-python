import json
from openai import OpenAI
from pathlib import Path
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional
from playsound3 import playsound
import requests

load_dotenv()

client = OpenAI()

def get_weather(city: str) -> str:
    """ Get weather details using city name """
    print(f"🔨 Tool Called: get_weather with input: {city}")
    
    url = f'https://wttr.in/{city}?format=%C+%t'
    response = requests.get(url)
    
    if response.status_code == 200:
        return f"The current weather of {city} is {response.text}"
    
    return f'Error fetching weather for {city}'

def convert_text_to_speech(text: str):
    """ Convert text to speech and save it as an audio file """
    
    speech_file_path = Path(__file__).parent / "speech.mp3"
    
    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="marin",
        input=text,
        instructions="Speak in a cheerful and positive tone in Hindi Language.",
    ) as response:
        response.stream_to_file(speech_file_path)
    
        print(f"🔊 Audio saved at: {speech_file_path}")
        playsound(speech_file_path)

class MyClass(BaseModel):
    step: str = Field(..., description="This is the ID of step")
    content: str = Field(..., description="This is process of the AI.")
    tool: Optional[str] = Field(None, description="tool name of the function")
    input: Optional[str] = Field(None, description="function parameter which we have to pass")
    output: Optional[str] = Field(None, description="function return value")

SYSTEM_PROMPT="""
    You're an AI Assistant in resolving user query using chain of thoughts.
    You have to work on START, PLAN and OUTPUT mode.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    
    Once you think enough then give me output.
    
    Rules:-
    - Strictly follow the given JSON Format
    - Only run one step at a time
    - The sequence of step is START (where user gives an INPUT), PLAN (That can be multiple time), ACTION (Tool calling), OBSERVE (result of the tool call appending by the user after getting the result) and OUTPUT (which is going to displayed to the user.)
    
    
    Available Tools:
    - get_weather(city: str) -> str: Get weather details using city name
    
    Output JSON Format:- 
    {
        'step': 'START' | 'PLAN' | 'ACTION' | 'OBSERVE' | 'OUTPUT'
        'content': 'string'
        'tool': 'string'
        'input': 'string'
        'output': 'string'
    }
    
    Example:- 
    Q:- How to make chai?
    Answer:- 
    START: { step: 'START', content: 'How to make chai?' }
    PLAN: { step: 'PLAN', content: 'User is asking cooking related question.' }
    PLAN: { step: 'PLAN', content: 'for making tea we have to bring water, milk, sugar and tea leaves.' }
    PLAN: { step: 'PLAN', content: 'First we need to boil water.' }
    PLAN: { step: 'PLAN', content: 'Then add tea leaves into the boiling water.' }
    PLAN: { step: 'PLAN', content: 'Now, add sugar according to the water.' }
    PLAN: { step: 'PLAN', content: 'After that, pour milk into the mixture.' }
    PLAN: { step: 'PLAN', content: 'Let it boil for 2-3 minutes so flavor mixes well.' }
    PLAN: { step: 'PLAN', content: 'Finally, strain the tea into a cup.' }
    PLAN: { step: 'PLAN', content: 'Tea is ready to be served hot.' }
    OUTPUT: { step: 'OUTPUT', content: 'Boil water, add tea leaves, sugar and milk cook for 2-3 minutes, strain and serve hot.' }
    
    Q:- What is weather of mumbai?
    Answer:- 
    START: { step: 'START', content: 'What is weather of Mumbai?' }
    PLAN: { step: 'PLAN', content: 'ok user is interested to know the weather information.' }
    PLAN: { step: 'PLAN', content: 'First I need to check available tool so that I can give the weather info' }
    PLAN: { step: 'PLAN', content: 'Ok I have get_weather tool to get weather info of particular city.' }
    PLAN: { step: 'PLAN', content: 'Now I have to check that this tool that how many parameter it is accepting' }
    PLAN: { step: 'PLAN', content: 'Ok, Great it is accepting one parameter which is city name.' }
    PLAN: { step: 'PLAN', content: 'Now I have to call the tool with the city name as input.' }
    PLAN: { step: 'ACTION', 'tool': 'get_weather', 'input': 'mumbai' }
    PLAN: { step: 'OBSERVE', 'output': '30C' }
    PLAN: { step: 'PLAN', content: 'ok the weather of mumbai is 30C.' }
    OUTPUT: { step: 'OUTPUT', content: 'The weather of mumbai is 30C please take some water and wear full t shirt.' }
"""

available_tools={
    'get_weather': get_weather
}

message_history=[
    { 'role': 'system', 'content': SYSTEM_PROMPT },
]

user_query = input("Enter your input: ")
message_history.append({ 'role': 'user', 'content': user_query })

while True:
    response = client.responses.parse(
        model='gpt-5.4-nano',
        text_format=MyClass,
        input=message_history
    )
    
    raw_result = response.output_text
    message_history.append( { 'role': 'assistant', 'content': raw_result } )
    parsed_result = response.output_parsed
    
    step = parsed_result.step
    content = parsed_result.content
    
    if step == 'START':
        print(f"🔥: {content}")
        continue
    
    if step == 'PLAN':
        print(f"🧠: {content}")
        continue
    
    if step == 'ACTION':
        function_name = parsed_result.tool
        function_input = parsed_result.input
        
        print(f"🔨 Tool Called: {function_name} with input: {function_input}")
        
        if available_tools[function_name]:
            function_output = available_tools[function_name](function_input)
        else:
            function_output = 'Error: Tool is not available'
        
        message_history.append( { 'role': 'assistant', 'content': json.dumps({ step: 'OBSERVE', 'output': function_output }) } )
        continue

    if step == 'OUTPUT':
        print(f"🤖: {content}")
        
        convert_text_to_speech(content)
        break
        
        