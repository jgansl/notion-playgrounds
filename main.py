import os
from os import environ, getenv

from notion_client import Client
notion = Client(auth=os.environ["NOTION_TOKEN"])

from notion_client import AsyncClient
notion = AsyncClient(auth=os.environ["NOTION_TOKEN"])