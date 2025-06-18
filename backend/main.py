from fastapi.responses import StreamingResponse
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from starlette.concurrency import run_in_threadpool

from typing import Dict

from data.RequestData import QueryData
from utils.GetResponse import SendResponse


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


@app.post("/")
async def query(query: QueryData):
  """Get response of user query from a select model

  Returns:
      str: A string of text from the model
  """
  return StreamingResponse(
    SendResponse(query),
    media_type="text/plain",
    headers= {
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
    }
  )

if __name__ == '__main__':
  import uvicorn
  uvicorn.run(app, host="127.0.0.1", port=8000)