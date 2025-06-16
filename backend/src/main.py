from fastapi.responses import StreamingResponse
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

from typing import Dict

from data.RequestData import QueryData


app = FastAPI()

origins = [
  "http://localhost:8000",
  "http://localhost"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)


@app.get("/")
def query(query: QueryData = Body(..., embed=True)) -> str:
  """Get response of user query from a select model

  Returns:
      str: A string of text from the model
  """
  try:
    json_query = query.model_dump(mode="json")
    
    pass
  except Exception as e:
    return str(e)
  
  return ''