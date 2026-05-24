import json
import os
from pathlib import Path

from anthropic import Anthropic

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

agent_id = json.loads(Path(".output/create_agent.json").read_text())["id"]
environment_id = json.loads(Path(".output/create_environment.json").read_text())["id"]

session = client.beta.sessions.create(
    agent=agent_id,
    environment_id=environment_id,
)

output_path = Path(".output/create_session.json")
output_path.parent.mkdir(exist_ok=True)

with output_path.open("w", encoding="utf-8") as f:
    json.dump(session.model_dump(mode="json"), f, ensure_ascii=False, indent=2)

print(session.id)
print(output_path)
