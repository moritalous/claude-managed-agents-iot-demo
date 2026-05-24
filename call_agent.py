import json
import os
import threading
import time
from pathlib import Path

from anthropic import Anthropic

client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

session_id = json.loads(Path(".output/create_session.json").read_text())["id"]
message = "Please blink the red LED three times."


def send_prompt() -> None:
    time.sleep(0.2)
    client.beta.sessions.events.send(
        session_id,
        events=[
            {
                "type": "user.message",
                "content": [
                    {
                        "type": "text",
                        "text": message,
                    }
                ],
            }
        ],
    )


events = []
sender = threading.Thread(target=send_prompt, daemon=True)


def is_finished(payload: dict) -> bool:
    return (
        payload.get("type") == "session.status_idle"
        and payload.get("stop_reason", {}).get("type") == "end_turn"
    ) or payload.get("type") in {
        "session.status_terminated",
        "session.status_rescheduled",
        "session.deleted",
        "session.error",
    }


with client.beta.sessions.events.stream(session_id) as stream:
    sender.start()
    for event in stream:
        payload = event.model_dump(mode="json")
        events.append(payload)
        print(json.dumps(payload, ensure_ascii=False))
        if is_finished(payload):
            break

sender.join()

output_path = Path(".output/call_agent.json")
output_path.parent.mkdir(exist_ok=True)

with output_path.open("w", encoding="utf-8") as f:
    json.dump(events, f, ensure_ascii=False, indent=2)

print(output_path)
