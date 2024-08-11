from fastapi import APIRouter
from api.v100.routes.redis_api import router as router_redis

router = APIRouter()

router.include_router(router_redis, prefix="/v100")
