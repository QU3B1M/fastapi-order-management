from fastapi import HTTPException, status


# Security Exceptions.

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

unauthorized_user_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="User not authorized for this action.",
    headers={"WWW-Authenticate": "Bearer"},
)

incorrect_password_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Incorrect username or password",
    headers={"WWW-Authenticate": "Bearer"},
)
