from fastapi import HTTPException, Request
from functools import wraps
from typing import Callable
from dotenv import load_dotenv
from XpenseMeter.core.security import decode_access_token

# Load environment variables
load_dotenv()

def token_authentication_required(func: Callable):
    """
    Decorator to enforce token-based authentication on a route.
    Args:
        func (Callable): The function to be decorated.
    Returns:
        Callable: The wrapped function.
    """

    @wraps(func)
    async def wrapped_function(request: Request, *args, **kwargs):
        # Extract the Authorization header.
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")

        token = auth_header.split(" ")[1]
        payload = decode_access_token(token)
        
        if not payload:
            raise HTTPException(status_code=401, detail="Invalid token or token has expired")

        request.state.email = payload.get('email')

        return await func(request, *args, **kwargs)

    return wrapped_function