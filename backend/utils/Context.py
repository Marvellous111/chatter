from openai import OpenAI
from typing import Optional
from data.RequestData import QueryData
from dotenv import load_dotenv
import os
from prompts.context import context_prompt

load_dotenv()

def man_context(query: str) -> str:
  openrouter_key = os.getenv("OPENROUTER_KEY")
  try:
    client = OpenAI(
      
    )
    return ''
  except Exception as e:
    return str(e)
