from fastapi import FastAPI

app = FastAPI(
    title="FinBud",
    summary="API for managing personal finances",
    description="user services for personal finance management",
    version="0.1.0",
    contact={},
    license_info={}
)

@app.get("/")
def home():
    return {"message": "Welcome to the personal finance API!"}
