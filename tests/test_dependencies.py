#import os
from os import environ, getenv
from pprint import pprint

from dotenv import load_dotenv
load_dotenv()#'../.env.development')

from notion_client import Client#, AsyncClient
import openai
openai.api_key = environ["OPENAI_API_KEY"]

def test_openai():
   models = openai.Model.list()

def test_notion():
   notion = Client(auth=environ["NOTION_TOKEN"])
   # notion = AsyncClient(auth=environ["NOTION_TOKEN"])
   list_users_response = notion.users.list()
   pprint(list_users_response)