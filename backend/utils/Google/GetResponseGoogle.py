from openai import OpenAI
from typing import Optional
from data.RequestData import QueryData
from dotenv import load_dotenv
import os
from prompts.system import system_prompt


load_dotenv()

def SendGeminiResponse(query):
  gemini_key = os.getenv("GEMINI_KEY")
  try:
    client = OpenAI(
      base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
      api_key=gemini_key
    )
    stream = client.chat.completions.create(
      model=query.model_used,
      reasoning_effort="low",
      messages= [
        {
          "role": "system",
          "content": system_prompt
        }, 
        {
          "role": "user",
          "content": query.content
        }
      ],
      stream=True
    )
        
    for chunk in stream:
      if chunk.choices[0].delta.content is not None:
        yield chunk.choices[0].delta.content + ""
  except Exception as e:
    yield f"Error: {str(e)}"