# import os
from os import environ, getenv
from dotenv import load_dotenv
load_dotenv()

import openai
openai.api_key = environ["OPENAI_API_KEY"]

from notion_client import Client#,AsyncClient
notion = Client(auth=environ["NOTION_TOKEN"])
# notion = AsyncClient(auth=environ["NOTION_TOKEN"])

models = openai.Model.list()

print(models.data[0].id)

# create a chat completion
chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

# print the chat completion
print(chat_completion.choices[0].message.content)