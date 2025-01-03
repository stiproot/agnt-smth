from typing import Tuple, Optional
from langchain_core.tools import tool
from ..utls import log, exec_sh_cmd


@tool
def dotnet_build(proj_path: str) -> Tuple[str, str]:
    """Builds a project using the .NET CLI. Runs `dotnet build` in the project directory.

    Args:
      proj_path: The path to the .csproj file to build.

    Returns:
      Tuple[str, str]: A tuple, with the first value being the build output and the second the error, if there is one.
    """

    cmd = f"dotnet build {proj_path}"

    log(f"dotnet_build START. proj_path: {proj_path}, cmd: {cmd}")

    return exec_sh_cmd(cmd)
