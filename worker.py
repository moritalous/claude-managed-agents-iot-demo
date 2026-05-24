import asyncio
import logging
import os
from pathlib import Path

from anthropic import AsyncAnthropic

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)


async def main() -> None:
    client = AsyncAnthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    workdir = Path(__file__).resolve().parent / "workspace"
    workdir.mkdir(exist_ok=True)
    worker = client.beta.environments.work.worker(
        environment_id=os.environ["ANTHROPIC_ENVIRONMENT_ID"],
        environment_key=os.environ["ANTHROPIC_ENVIRONMENT_KEY"],
        workdir=workdir,
    )
    await worker.run()


if __name__ == "__main__":
    asyncio.run(main())
