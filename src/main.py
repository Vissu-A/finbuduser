'''
Main module for the personal finance API.
'''

# standard imports
from fastapi import FastAPI

# third-party imports

# internal imports
from src.routers.v1.user_router import router as u_router

app = FastAPI(
    title="FinBud",
    summary="API for managing personal finances",
    description="user services for personal finance management",
    version="0.1.0",
    contact={},
    license_info={}
)

# including user routers defined in routers module
app.include_router(u_router)
