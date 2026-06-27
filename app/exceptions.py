from fastapi import HTTPException

class VideoNotFound(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=404, 
            detail="Video not found")

class TranscriptUnavailable(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=422, 
            detail="Transcript not available for this video"
            )

class InvalidYoutubeURL(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=422, 
            detail="Invalid or unsupported YouTube URL"
            )

class ExternalServiceError(HTTPException):
    def __init__(self, service: str):
        super().__init__(
            status_code=503,
            detail=f"{service} is currently unavailable. Please try again later."
        )

class UserNotFound(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail="User not found"
        )

class InvalidTokenError(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=401,
            detail="Invalid Token"
        )

class ChatSessionNotFound(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=404,
            detail="Chat session not found"
        )

class VideoAlreadyProcessed(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=409,
            detail="Video already exists and has been processed"
        )