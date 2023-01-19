import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def validate(s: str):
    prompt = "Is this the right format for a romanian license plate number?\n" + s
    # if len(s) != 9:
    #     return False
    #
    # if not s[:2].isalpha():
    #     return False
    #
    # if s[2] != '-' or s[5] != '-':
    #     return False
    #
    # if not s[6:].isalpha():
    #     return False
    #
    # return response.choices[0].text

    response = openai.Completion.create(prompt=prompt, temperature=1, max_tokens=1000, model="text-davinci-003")

    print(response.choices[0].text)

# validate("SB1234AB")

def pig(s):
    print(openai.Completion.create(prompt="Write this in pig latin: " + s, temperature=0.1, max_tokens=1000, model="text-davinci-003").choices[0].text)


pig("naomi")