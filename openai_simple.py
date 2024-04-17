import openai
import getpass
import os

# Set your API key here
token = getpass.getpass(prompt='OpenAI token: ')
os.environ['OPENAI_API_KEY'] = token

from openai import OpenAI
model = "gpt-3.5-turbo"
# model="gpt-4-turbo"
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Can you describe what an ordinary differential equation is, and provide a couple of examples.",
        }
    ],
    model = model,
)

print(f'{chat_completion.choices[0].message.content}')
