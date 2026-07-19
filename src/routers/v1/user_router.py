'''
user routers module
'''

# Standard Python imports

# Fast api imports
from fastapi import APIRouter
from fastapi import status

# Third party modules import

# internal imports
from src.schemas.user_schema import CreateUserSchema

# creating Api router object
router = APIRouter(
    prefix="/user",
    tags=["user_management"]
)


# Defining user routers
@router.get(
    path="",
    summary="user home",
    status_code=status.HTTP_200_OK
)
def user_home() -> dict:
    '''
    router for user home.
    '''
    return {"message": "Welcome to the personal financing API!"}


# New user creation: signup
@router.post(
    path="/signup",
    summary="New user creation.",
    status_code=status.HTTP_201_CREATED
)
def create_user(userdata: CreateUserSchema):
    '''Creating a new user account'''

    return {
        "message": "User deatils received successfully.",
        "data": userdata
    }
