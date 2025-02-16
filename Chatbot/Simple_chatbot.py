import openai

openai.api_key = "insert_api_key_here"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role":"user", "content":"write prompt here"}])

print(completion.choices[0].message.content.Strip())

        

