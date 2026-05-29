'''
user routers module
'''

from fastapi import APIRouter
from fastapi import status

# creating Api router object
router = APIRouter(
    prefix="/user",
    tags=["user_management"]
)


# Defining user routers
@router.get(
    path="/",
    summary="user home",
    status_code=status.HTTP_200_OK
)
def user_home() -> dict:
    '''
    router for user home.
    '''
    return {"message": "Welcome to the personal financing API!"}
