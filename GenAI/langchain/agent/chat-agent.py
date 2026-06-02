from langchain.agents import create_agent
from langchain.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

agent = create_agent(
    model='gpt-4o-mini'
)

result = agent.invoke({"messages": HumanMessage('What is full name of gandhi ji.')})

print(result['messages'][-1].content)