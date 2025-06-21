import redis
from fastapi import HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")
redis_time_limit = os.getenv("RATE_LIMIT")
redis_window_seconds = os.getenv("TIME_WINDOW")

r= redis.Redis(host=redis_host, port=6379, db=0)

def rate_limiter(uuid: str, limit: int, window_seconds: int):
  key = f"ratelimit:{uuid}"
  current = r.get(key)
  
  if current and int(current.decode()) >= limit:
    raise HTTPException(status_code=429, detail="Rate limit reached")
  
  pipe = r.pipeline()
  pipe.incr(key, 1)
  pipe.expire(key, window_seconds)
  pipe.execute()