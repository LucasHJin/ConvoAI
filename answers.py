import openai
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
# prompts = [
#     "Tell me a joke.",
#     "Can you share a funny joke?",
#     "What's a good joke you know?",
#     "Do you know any jokes?"
# ]


# prompt = random.choice(prompts)


# conversation = [
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": prompt}
# ]


# # response = openai.ChatCompletion.create(
# #     model="gpt-4",
# #     messages=conversation,
# #     temperature=0.7
# # )


# print(response.choices[0].message['content'])


# # Adding follow-up conversation
# conversation.append({"role": "assistant", "content": response.choices[0].message['content']})
# conversation.append({"role": "user", "content": "Can you tell me another joke?"})


# # response = openai.ChatCompletion.create(
# #     model="gpt-4",
# #     messages=conversation,
# #     temperature=0.7
# # )


# print(response.choices[0].message['content'])


def comp(PROMPT, MaxToken=50, outputs=1):
    # using OpenAI's Completion module that helps execute  
    # any tasks involving text  
    response = openai.ChatCompletion.create(
        # model name used here is text-davinci-003
        # there are many other models available under the  
        # umbrella of GPT-3
        model="gpt-3.5-turbo",
        # passing the user input  
        messages=[PROMPT],
        temperature=0.7
        # generated output can have "max_tokens" number of tokens  
        # max_tokens=MaxToken,
        # number of outputs generated in one call
        # n=outputs
    )
    # creating a list to store all the outputs
    output = list()
    for k in response['choices']:
        output.append(k['text'].strip())
    return output


# print(comp('Tell me a joke.'))

