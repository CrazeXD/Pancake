from openai import OpenAI
import os

import pathlib
api_key = pathlib.Path("main/info/api_key.txt").read_text().strip()
client = OpenAI(api_key=api_key)
# TODO: Fine-tune the prompt and the temperature for better results
system_prompt = pathlib.Path("main/info/prompt.txt").read_text()

def get_response(prompt, known_technologies):
    full_prompt = f'''
    IDEA: {prompt}
    Known Technologies: {', '.join(known_technologies)}
    '''

    # Call the OpenAI API for GPT-3.5 Turbo with the system prompt and the full prompt
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": full_prompt},
        ],
        max_tokens=100,
        temperature=1,
    )
    response = response.choices[0].message.content
    # Turn the response into a dictionary from a string where each new line is 'key: value'
    response = response.split('\n')
    response = [line.strip() for line in response if line]
    return response
