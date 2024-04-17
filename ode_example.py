### ODE PROPMTS
import openai
import getpass
import os
import sys
from openai import OpenAI


# ode = sys.argv[1]
ode = {
        "name": "Newton's Second Law of Motion",
        "equation": "d2x/dt2 = F/m",
        "description": "Describes the motion of a body under the influence of external forces."
}

# model = "gpt-3.5-turbo"
model = "gpt-4-turbo"

token = getpass.getpass(prompt='OpenAI token: ')
os.environ['OPENAI_API_KEY'] = token

prompts_start=[
    {"role": "system", "content": "You are a numerical algorithms assistant, skilled in explaining complex programming concepts in python"},
    {"role": "user", "content": "What is an ordinary differential equation."}
  ]

prompts_run = [
        {"role": "user", "content": "Can you solve this ordinary differential equation: dxdt=0"},
        {"role": "user", "content": "Can you solve this ODE: dxdt=msint+nt3"},
        {"role": "user", "content": f"Can you solve this ODE: {ode}"},
        {"role": "user", "content": f"This is great. Can you generate the python code to solve this ODE: {ode}?"},
        {"role": "user", "content": "In the context of the current discussion, what is a discretization?"},
        {"role": "user", "content": "Where does the discretization occur in the python code that you generated?"},
        {"role": "user", "content": "And in the context of the current discussion what a solver is?"},
        {"role": "user", "content": "In the example above, could you provide the equations of the edge cases?"},
        {"role": "user", "content": "Can you generate the code for these edge cases?"},
]

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

prompts = prompts_start
print(f"initializing conversation\n\n")
print(f"{prompts_start[1]["content"]}\n\n")

chat_completion = client.chat.completions.create(
        messages = prompts,
        model = model,
    )

response = chat_completion.choices[0].message.content
prompts.append({"role": "assistant", "content": response})
print(f'{response}\n\n')

for i in range(0, len(prompts_run)):
    print(f"{prompts_run[i]["content"]}\n\n")
    prompts.append(prompts_run[i])
    chat_completion = client.chat.completions.create(
        messages = prompts,
        model = model,
    )
    response = chat_completion.choices[0].message.content
    print(f'{response}\n\n')
    prompts.append({"role": "assistant", "content": response})

print(f'\n\n\n{prompts}')

