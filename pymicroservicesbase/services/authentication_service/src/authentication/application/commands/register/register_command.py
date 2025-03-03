from pydantic import ConfigDict, EmailStr
from typing import Annotated
from fastapi import Body, Depends, Query, Response, Request

from pymicroservicesbase.sdk.web_api.core_api.base_web_command import (
    BaseWebCommand,
)


class RegisterCommand(BaseWebCommand):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    username: str
    password: str
    register_method: str
    email: EmailStr
    response: Response
    request: Request


async def get_register_command(
    response: Response,
    request: Request,
    username: str = Body(default="test"),
    password: str = Body(default="test"),
    email: EmailStr = Body(default="test@test.com"),
    register_method: str = Query(default="instant"),
) -> RegisterCommand:
    return RegisterCommand(
        request=request,
        response=response,
        username=username,
        password=password,
        email=email,
        register_method=register_method,
    )


RegisterCommandDep = Annotated[RegisterCommand, Depends(get_register_command)]
