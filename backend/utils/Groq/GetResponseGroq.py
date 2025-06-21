from openai import OpenAI
from typing import Optional
from data.RequestData import QueryData
from dotenv import load_dotenv
import os
from prompts.system import system_prompt


load_dotenv()

async def SendGroqResponse(query: QueryData):
  groq_key = os.getenv("GROQ_SECRET_KEY")
  try:
    client = OpenAI(
      base_url="https://api.groq.com/openai/v1",
      api_key=groq_key
    )
    stream = client.chat.completions.create(
      model=query.model_used,
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
