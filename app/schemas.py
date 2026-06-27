from datetime import datetime
from pydantic import BaseModel, ConfigDict
import uuid

#AUTH
class TokenResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    email: str
    display_name: str
    avatar_url: str


#VIDEOS

class VideoSubmitRequest(BaseModel):
    url: str


class VideoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    video_id: str
    title: str
    ai_summary: str | None = None
    processing_status: str
    created_at: datetime


class VideoStatusResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    processing_status: str


#CHAT
class ChatSessionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: uuid.UUID
    video_id: str
    created_at: datetime

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    answer: str
    session_id: uuid.UUID
    timestamp: int | None = None