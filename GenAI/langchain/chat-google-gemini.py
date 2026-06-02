from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Initialize the model
model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

# Messages History
messages = [
    ("system", "You are expert email writer."),
    ("human", "Write a 200 word email for wishing happy birthday."),
]

# print response without streaming
response = model.invoke(messages)
print(response.text)


# print response with streaming 
# for chunk in model.stream(messages):
#     print(chunk.text)