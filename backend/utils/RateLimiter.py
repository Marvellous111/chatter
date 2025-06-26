import redis
from fastapi import HTTPException
from dotenv import load_dotenv
import os
import redis.asyncio
from redis.cache import CacheConfig

load_dotenv()

try:
  redis_host = os.getenv("REDIS_HOST")
  redis_port = os.getenv("REDIS_PORT")
  redis_username = os.getenv("REDIS_USERNAME")
  redis_password = os.getenv("REDIS_PASSWORD")
    
  if redis_host is None:
    raise ValueError("Redis Host is missing from the environment, please fill it.")
  if redis_port is None:
    raise ValueError("Redis port is missing from the environment, please fill it.")
  if redis_username is None:
    raise ValueError("Redis username is missing from the environment, please fill it.")
  if redis_password is None:
    raise ValueError("Redis password is missing from the environment, please fill it.")
    
  r = redis.Redis(
    host=redis_host,
    port=int(redis_port),
    username= redis_username,
    password=redis_password,
    max_connections=5,
    cache_config = CacheConfig(),
    protocol=3,
    decode_responses=True,
    retry_on_timeout=True
  )
except ConnectionError as connection_error:
  raise ConnectionError(f"Connection error ocurred: {connection_error}")
except Exception as e:
  raise ValueError(f"An exception occured: {e}")


async def reset_limit(user_uuid: str):
  if user_uuid:
    redis_user_key = f"user_uuid:<{user_uuid}>"
    redis_user_content = r.set(redis_user_key, 10)
    return "Done"



async def ratelimit(user_uuid: str) -> int:
  if user_uuid:
    redis_user_uuid_key = f"user_uuid:<{user_uuid}>"
    redis_uuid_content = r.get(redis_user_uuid_key)
    if redis_uuid_content is None:
      rate_limit_number = 10
      try:
        r.set(redis_user_uuid_key, rate_limit_number)
        return rate_limit_number
      except ConnectionError as connection_error:
        raise ConnectionError(f"Connection pool is full, please wait a bit: {connection_error}")
    # We add type ignore there because await r.get() doesnt work and throws a bug, will test more to get into it more  
    current_limit = int(redis_uuid_content) # type: ignore
    print(f"Cuurent limit is: {current_limit}")
    if current_limit == 0:
      r.set(redis_user_uuid_key, 0)
      return 0
    new_limit = max(current_limit - 1, 0)
    r.set(redis_user_uuid_key, new_limit)
    return new_limit
  else:
    return -1


