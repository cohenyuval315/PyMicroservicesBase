from pymicroservicesbase.sdk.web_api.core_api.web_router import WebRouter
from pymicroservicesbase.sdk.web_api.common.logging.api.controllers.logging_controller_dep import (
    LoggingControllerDep,
)
from pymicroservicesbase.sdk.web_api.common.logging.application.commands.get_logs_command import (
    GetLogsCommand,
)

logging_router = WebRouter(prefix="/logging", tags=["logging"])


@logging_router.get("", status_code=200)
async def get_logs(
    command: GetLogsCommand, logging_controller: LoggingControllerDep
):
    return await logging_controller.get_logs(command)
