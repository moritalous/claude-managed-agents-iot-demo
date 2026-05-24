import json
import os
from pathlib import Path

from anthropic import Anthropic

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

agent = client.beta.agents.create(
    name="Raspberry Pi LED Assistant",
    model="claude-haiku-4-5",
    system=(
        "You are running on a Raspberry Pi.\n"
        "A red LED is connected to GPIO 17.\n"
        "When asked to control the LED, do so on that hardware.\n"
        "Write clean, well-documented code."
    ),
    tools=[{"type": "agent_toolset_20260401"}],
)

output_path = Path(".output/create_agent.json")
output_path.parent.mkdir(exist_ok=True)

with output_path.open("w", encoding="utf-8") as f:
    json.dump(agent.model_dump(mode="json"), f, ensure_ascii=False, indent=2)

print(agent.id)
print(output_path)
