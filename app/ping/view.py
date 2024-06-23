from fastapi import APIRouter

from app.ping.schema import PingResponse

router = APIRouter(tags=["healthcheck"])


@router.get("/ping", response_model=PingResponse)
def healthcheck():
    return PingResponse(message="pong")
