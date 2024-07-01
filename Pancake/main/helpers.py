from openai import OpenAI
import os

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def get_response(prompt):
    full_prompt = f'''
    Create a tech stack for the following project. Structure your response as the following.
    Layer: Technology
    Information about the technology

    Here is an example, however, when you are creating the tech stack, make sure to include all the necessary technologies for the project.
    Frontend: React
    Backend: Django
    Database: PostgreSQL

    IDEA: {prompt}
    '''

    response = client.complete(
        engine="gpt-4o",
        prompt=full_prompt,
        max_tokens=200,
    )
    return response.choices[0].text