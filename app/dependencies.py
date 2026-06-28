from app.database import SessionLocal
from app.auth.jwt import verify_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends

async def get_db():
    async with SessionLocal() as session:
        yield session

security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = verify_token(token)
    return payload