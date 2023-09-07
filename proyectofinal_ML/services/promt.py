from services.text_speech import *
import openai
def explicar(gpt_prompt: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=gpt_prompt,
        temperature=0.8,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    text_to_speech(response['choices'][0]['text'])
    return response['choices'][0]['text']


def codigo(gpt_prompt: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=gpt_prompt,
        temperature=0.8,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    return response['choices'][0]['text']

def ejercicios(gpt_prompt: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=gpt_prompt,
        temperature=0.8,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    return response['choices'][0]['text']