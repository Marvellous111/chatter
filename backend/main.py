from fastapi.responses import StreamingResponse
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from starlette.concurrency import run_in_threadpool
import uuid

from typing import Dict

from data.RequestData import QueryData
from utils.Groq.GetResponseGroq import SendGroqResponse
from utils.Google.GetResponseGoogle import SendGeminiResponse
# from utils.RateLimiter import rate_limiter


app = FastAPI()

origins = [
  "http://localhost:8000",
  "http://localhost"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

@app.get("/generate-unsignedid")
def generate_id():
  user_id = str(uuid.uuid4())
  return {
    "uuid": user_id
  }
  

@app.post("/")
async def query(query: QueryData):
  """Get response of user query from a select model

  Returns:
      str: A string of text from the model
  """
  if query.model_provider.lower() == "groq":
    return StreamingResponse(
      SendGroqResponse(query),
      media_type="text/plain",
      headers= {
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
      }
    )
  elif query.model_provider.lower() == "google":
    return StreamingResponse(
      SendGeminiResponse(query),
      media_type="text/plain",
      headers= {
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
      }
    )

if __name__ == '__main__':
  import uvicorn
  uvicorn.run(app, host="127.0.0.1", port=8000)