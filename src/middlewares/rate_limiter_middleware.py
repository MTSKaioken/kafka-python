from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request


class RateLimiterMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print('caiu')
        response = await call_next(request)
        print('respondeu')
        return response
