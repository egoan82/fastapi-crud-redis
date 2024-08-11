from fastapi import APIRouter, status, Depends, HTTPException
from typing import Annotated
from fastapi.params import Query
from dependencies.redis import RedisClient

router = APIRouter()


@router.get(
    "/search",
    status_code=status.HTTP_200_OK,
    summary="Search for a key in Redis",
)
def list_all(
        search: Annotated[str, Query(description="Search for a key in Redis by pattern (key*)")],
        client: RedisClient = Depends(RedisClient)
):
    try:
        return client.search_pattern(pattern=search)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e.args[0])
        )


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    summary="Create key-value in Redis",
)
def create(
        key: Annotated[str, Query(description="Key to create in Redis")],
        value: Annotated[str, Query(description="Value to create in Redis")],
        client: RedisClient = Depends(RedisClient)
):
    try:
        client.set(key=key, value=value)
        return {"message": "created successfully"}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e.args[0])
        )


@router.get(
    "/get_by_key/{key}",
    status_code=status.HTTP_200_OK,
    summary="Get by key from Redis",
)
def get_by_key(
        key: Annotated[str, "Get value by key from Redis"],
        client: RedisClient = Depends(RedisClient)
):
    try:
        return client.get(key=key)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e.args[0])
        )


@router.delete(
    "/delete/{key}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete by key from Redis",
)
def delete(
        key: Annotated[str, "Delete by key from Redis"],
        client: RedisClient = Depends(RedisClient)
):
    try:
        client.delete(key=key)
        return {"message": "deleted successfully"}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e.args[0])
        )
