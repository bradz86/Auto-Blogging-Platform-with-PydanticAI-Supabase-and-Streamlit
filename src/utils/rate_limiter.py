"""
    Rate Limiter Implementation
    """
    from fastapi import HTTPException, Request
    from slowapi import Limiter
    from slowapi.util import get_remote_address
    from src.config.production import settings

    limiter = Limiter(key_func=get_remote_address)

    def rate_limit_exceeded_handler(request: Request, exc: HTTPException):
        return HTTPException(
            status_code=429,
            detail="Too many requests. Please try again later."
        )
