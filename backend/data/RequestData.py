from pydantic import  BaseModel
from datetime import datetime
from typing import Optional

class QueryData(BaseModel):
  content: str
  modelUsed: str
  datetime: datetime
  attachment_status: str
  websearch: bool
  deepreasoning: bool