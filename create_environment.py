import json
import os
from pathlib import Path

from anthropic import Anthropic

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

environment = client.beta.environments.create(
    name="raspberry-pi-sandbox",
    config={"type": "self_hosted"},
)

output_path = Path(".output/create_environment.json")
output_path.parent.mkdir(exist_ok=True)

with output_path.open("w", encoding="utf-8") as f:
    json.dump(environment.model_dump(mode="json"), f, ensure_ascii=False, indent=2)

print(environment.id)
print(output_path)
