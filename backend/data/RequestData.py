from pydantic import  BaseModel
from datetime import datetime
from typing import Optional

class QueryData(BaseModel):
  content: str
  model_used: str
  model_provider: str
  attachment_status: bool
  websearch: bool
  deepreasoning: bool