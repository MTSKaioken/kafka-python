from collections import defaultdict
import time
from typing import Any, Dict

from fastapi import Request
from fastapi.responses import Response
from starlette import status
from starlette.middleware.base import BaseHTTPMiddleware


class RateLimiterMiddleware(BaseHTTPMiddleware):

    def __init__(self, app: Any) -> None:
        super().__init__(app)
        self.rate_limit_records: Dict[str, float] = defaultdict(float)

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time.time()
        if current_time - self.rate_limit_records[client_ip] < 1:
            return Response(content="Rate limit exceeded", status_code=status.HTTP_429_TOO_MANY_REQUESTS)
        self.rate_limit_records[client_ip] = current_time
        response = await call_next(request)
        return response
        # hash = request.headers.get('Authorization')
        # if hash:
        #     response = await call_next(request)
        #     print('respondeu')
        #     return response
        # else:
        #     return Response(content="Usuario não autenticado", status_code=status.HTTP_401_UNAUTHORIZED)
