from fastapi.responses import StreamingResponse, Response
from fastapi import FastAPI, Body, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.concurrency import run_in_threadpool
import uuid
import jwt
import os
from dotenv import load_dotenv

from typing import Dict

from data.RequestData import QueryData
from utils.Groq.GetResponseGroq import SendGroqResponse
from utils.Google.GetResponseGoogle import SendGeminiResponse
from utils.RateLimiter import ratelimit, reset_limit


load_dotenv()

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
  allow_headers=["*"],
  expose_headers=[
    "x-ratelimit-id",
    "x-ratelimit-remaining"
  ]
)


@app.get('/reset-id')
async def reset_id(response: Response, request: Request):
  anon_request_header = request.headers.get("x-ratelimit-id")
  if anon_request_header is None:
    raise ValueError("The request header is missing.")
  secret_key = os.getenv("CHATTER_SECRET_KEY")
  if secret_key is None:
    raise ValueError("The secret key is missing, add a secret key to the environment")

  decoded_anon_request_header = jwt.decode(anon_request_header, secret_key, ["HS256"])
  reset_rate_limit = reset_limit(decoded_anon_request_header['user_uuid'])
  if reset_rate_limit == "Done":
    return {
      "reset_message": "Done"
    }


@app.get("/generate-id")
async def generate_id(response: Response):
  user_uuid = str(uuid.uuid4())
  PAYLOAD = {
    "user_uuid": user_uuid
  }
  secret_key = os.getenv("CHATTER_SECRET_KEY")
  if secret_key is None:
    raise ValueError("CHATTER_SECRET_KEY is not found in the environment, consider adding a secret key to the environment")
  encoded_jwt = jwt.encode(PAYLOAD, secret_key, algorithm="HS256")
  rate = await ratelimit(user_uuid)
  response.headers["x-ratelimit-remaining"] = str(rate)
  return {
    "uuid": encoded_jwt
  }
  

@app.post("/")
async def query(request: Request, query: QueryData):
  """Get response of user query from a select model

  Returns:
      str: A string of text from the model
  """
  anon_request_header = request.headers.get('x-ratelimit-id')
  
  if anon_request_header is None:
    raise ValueError("The request header is missing, please include it in the header")
  secret_key = os.getenv("CHATTER_SECRET_KEY")
  if secret_key is None:
    raise ValueError("CHATTER_SECRET_KEY is not found in the environment, consider adding a secret key to the environment")
  
  decoded_anon_request_header = jwt.decode(anon_request_header, secret_key, ["HS256"])
  rate_limit = await ratelimit(decoded_anon_request_header["user_uuid"])
  if rate_limit == 0:
    return Response(
      status_code= 429,
      content = "Rate limit reached"
    )
    
  response_headers = {
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "x-ratelimit-remaining": f"{rate_limit}"
  }
  
  if query.model_provider.lower() == "groq":
    return StreamingResponse(
      SendGroqResponse(query),
      media_type="text/plain",
      headers= response_headers
    )
  elif query.model_provider.lower() == "google":
    return StreamingResponse(
      SendGeminiResponse(query),
      media_type="text/plain",
      headers= response_headers
    )

if __name__ == '__main__':
  import uvicorn
  uvicorn.run(app, host="127.0.0.1", port=8000)