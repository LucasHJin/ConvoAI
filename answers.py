"""
"""
import openai

openai.api_key = 'your-api-key-here'

conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me a joke."}
]

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=conversation
)

print(response.choices[0].message['content'])

# Add the assistant's response to the conversation
conversation.append({"role": "assistant", "content": response.choices[0].message['content']})

# Continue the conversation
conversation.append({"role": "user", "content": "Can you tell me another one?"})

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=conversation
)

print(response.choices[0].message['content'])


