import os
import openai

root = "../praktisch/"


def clean_req():
    req = root + "req.txt"

    with open(req, 'r') as f:
        content = f.read()
        content = content.replace("#", "")
        start = content.find("1.\n")
        content = content[start:]

        ex1 = content.find("1.")
        ex2 = content.find("2.")
        ex3 = content.find("3.")
        ex_list = [content[ex1:ex2], content[ex2:ex3], content[ex3:]]

    return ex_list


def solve(file, prompt):
    response = openai.Completion.create(prompt=prompt, temperature=0, max_tokens=1500, model="text-davinci-003")
    with open(file, 'w') as f:
        f.write(response.choices[0].text)


def write_code():
    ex_list = clean_req()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    p1 = ex_list[0] + "\nDo not use loops, use python functions like map, filter, reduce and lambdas"
    solve("one.py", p1)

    solve("two.py", ex_list[1])
    solve("three.py", ex_list[2])


# write_code()

prompt = "Eine Routine hat 16.000 CPU-Anweisungen. Der Befehlssatz der CPU hat eine CPI-Wert von 5. "\
    "Mit welcher Taktfrequenz muss die CPU getaktet sein, damit die Routine nicht länger als 6ms dauert? "\
    "Mit Erklärung"

response = openai.Completion.create(prompt=prompt, temperature=1, max_tokens=1500, model="text-davinci-003")

print(response.choices[0].text)