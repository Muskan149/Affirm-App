import openai
import os
import json

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.environ.get('OPENAI_API_KEY')


def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def return_affirmations(grievance, temperature=0):
    PROMPT = f"""
    You are a positive affirmations generator. Your task is to generate positive, credible, and achievable \ 
    affirmation statements that will help alleviate the user's problems/grievances.

    Generate a Python list of 3 affirmations, each affirmation not more than 15 words, \
    for mitigating the user's grievance. The affirmations should not be arbitrary; \
    they should be specific to the user's grievance. 

    Here is the user's grievance, delimited by three backticks: ```{grievance}```

    Generate the  affirmations  in the JSON format with the key "affirmations"."""

    response = get_completion(PROMPT, temperature=temperature)
    response_dict = json.loads(response)
    three_affirmations = response_dict["affirmations"]

    return three_affirmations
