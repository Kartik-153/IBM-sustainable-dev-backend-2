from fastapi import APIRouter

entry_root = APIRouter()

# endpoint of the api
@entry_root.get("/")
def apiRunning():
    res = {
        "status": "ok",
        "message": "Api is running"
    }
    return res