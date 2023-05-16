import openai
import os
import json

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

PROMPT = f"""
You are a positive affirmations generator. Your task is to generate empowering affirmations that will help mitigate the user's problems/grievances. 

Generate a Python list of 3 positive affirmations, each affirmation not more than 15 words, for mitigating the user's grievance. The affirmations should not be arbitrary; they should be specific to the user's grievance. 

Here is the user's grievance, delimited by three backticks: ```{grievance}```

Generate the  affirmations  in the JSON format with the key "three_affirmations"."""

response = get_completion(PROMPT)
response_dict = json.loads(response)
three_affirmations = response_dict["three_affirmations"]

