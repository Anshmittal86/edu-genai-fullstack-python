from langchain.agents import create_agent
from langchain.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

# Initialize the agent 
# This automatically handles the tool-calling loop
agent = create_agent(model='gpt-4o-mini')

# Invoke the agent
result = agent.invoke({"messages": [HumanMessage('What is full name of gandhi ji.')]})

# Access the content from the final message in the state
print(result['messages'][-1].content)