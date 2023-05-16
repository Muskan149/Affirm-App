import openai
import os

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


lamp_review = f"""
You are a positive affirmations generator. \
Your task is to generate empowering affirmations that will help mitigate the user's problems/grievances. 

Generate a list of 3 positive affirmations, each affirmation not more than 20 words, \
for mitigating the user-grievance which is delimited with triple backticks. \
The affirmations should not be arbitrary; \
they should be specific to the user's grievance. 

Here is the user's grievance: {grievance}.

Generate the  affirmations  in the JSON format with the keys "grievance" and "three_affirnations". "
"""

response = get_completion(prompt)
print(response)