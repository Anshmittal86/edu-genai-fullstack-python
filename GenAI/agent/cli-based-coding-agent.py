import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional
from pathlib import Path
import subprocess

load_dotenv()

client = OpenAI()


def read_file(file_path: str) -> str:
    """ Reading file using file path """
    print(f"🔨 Tool Called: read_file: {file_path}")
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"❌ Error Reading files: {str(e)}"
    
def write_file(input_json: str) -> str:
    """ Writing the file """
    print(f"🔨 Tool Called: read_file: {input_json[:200]}...")
    
    try:
        params = json.loads(input_json)
    except json.JSONDecodeError as e:
        return f"❌ JSON Error: {str(e)[:100]}. Input was malformed"
    
    file_path = params.get('file_path', 'Not Found')
    content = params.get('content')
    
    if not file_path or content is None:
        return f"❌ Missing file_path and content in params."
    
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    
    try:
        with open(file_path, 'w') as f:
            f.write(content)
            return f'✅ File written: {file_path}'
    except Exception as e:
        return f"❌ Written error: {str(e)}"
    

def list_directory(dir_path: str) -> str:
    """ Lists files and directories in the given path. """
    print(f"🔨 Tool Called: list_directory {dir_path}")
    
    try:
        items = os.listdir(dir_path)
        return "\n".join(items)
    except Exception as e:
        return f'Error listing Directory: {str(e)}'

def run_shell(input_json: str) -> str:
    print(f"🔨 Tool Called: run_shell {input_json[:200]}...")
    
    params = json.loads(input_json)
    cmd = params['cmd']
    
    try: 
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True, 
            timeout=30
        )
        output = result.stdout + result.stderr
        return f"Exist code {result.returncode}\nOutput:{output}"
    
    except subprocess.TimeoutExpired as e:
        return f"Command Timed out"
    
    except Exception as e:
        return f"Error Running Command: {str(e)}"
        

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
    - If you are searching the file then not go directly the observe step because OBSERVE step is only given by me this is not user step.
    
    Available Tools:
    - read_file(file_path: str): Reads content form a file
    - write_file(input_json: str): { 'file_path': 'file.py', 'content': 'code here' }
    - run_shell(input_json: str): { 'cmd': 'ls', 'cwd': '.' }
    - list_directory(dir_path: str): Lists files in directory
    
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
    'read_file': read_file,
    'write_file': write_file,
    'list_directory': list_directory,
    'run_shell': run_shell
}


message_history=[
    { 'role': 'system', 'content': SYSTEM_PROMPT },
]

while True:
    user_query = input("Enter your input (exit for exit): ")
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
            
            if available_tools.get(function_name, False) != False:
                function_output = available_tools[function_name](function_input)
            else:
                function_output = 'Error: Tool is not available'
            
            message_history.append( { 'role': 'assistant', 'content': json.dumps({ step: 'OBSERVE', 'output': function_output }) } )
            continue

        if step == 'OUTPUT':
            print(f"🤖: {content}")
            break
        
    
    if user_query.lower == 'exit':
        break