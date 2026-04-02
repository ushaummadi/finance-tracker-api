from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth import verify_token

# Security scheme for Swagger
security = HTTPBearer()

ROLE_PERMISSIONS = {
    "viewer": ["read"],
    "analyst": ["read", "analytics"],
    "admin": ["read", "write", "analytics"]
}

def get_current_role(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials  # Extract token after "Bearer"
        payload = verify_token(token)

        if not payload:
            raise HTTPException(status_code=401, detail="Invalid token")

        return payload["role"]

    except Exception:
        raise HTTPException(status_code=401, detail="Authorization failed")


def check_permission(role: str, permission: str):
    if permission not in ROLE_PERMISSIONS.get(role, []):
        raise HTTPException(status_code=403, detail="Access Denied")