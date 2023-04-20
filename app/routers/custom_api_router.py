from fastapi import APIRouter, status

class CustomAPIRouter(APIRouter):
    def __init__(self, prefix): 
        super(CustomAPIRouter, self).__init__(
            prefix=f"/{prefix}",
            tags=[prefix], # type: ignore
            responses={
                status.HTTP_404_NOT_FOUND: {"description": "Not found"},
            },
        )