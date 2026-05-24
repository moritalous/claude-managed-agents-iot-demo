# claude-managed-agents-iot-demo

Raspberry Pi上のLEDをClaude Managed Agentsからの指示で光らせるためのデモです。

> [!NOTE]
> 日本語の解説のあとに英語版があります。
> The English version follows below.

## 日本語

### 事前準備

- Python 3.13
- `uv`
- `ANTHROPIC_API_KEY`
- `ANTHROPIC_ENVIRONMENT_ID`
- `ANTHROPIC_ENVIRONMENT_KEY`

まず`.env.sample`を`.env`にコピーして、必要な値を設定してください。

### 使い方

このプロジェクトは、次の順番で動かします。

1. Agentを作成する
2. Environmentを作成する
3. Workerを起動する
4. Sessionを作成する
5. Agentを呼ぶ

#### 1. Agentを作成する

```bash
uv run python create_agent.py
```

Agentの設定が`.output/create_agent.json`に保存されます。

#### 2. Environmentを作成する

```bash
uv run python create_environment.py
```

Environmentの設定が`.output/create_environment.json`に保存されます。

Claude Consoleで作成した環境を確認し、環境KEYを生成してください。

#### 3. Workerを起動する

以下の環境変数を設定します。

- `ANTHROPIC_ENVIRONMENT_ID`
- `ANTHROPIC_ENVIRONMENT_KEY`

```bash
uv run python worker.py
```

Workerは別ターミナルか別プロセスで起動したままにしてください。`ANTHROPIC_ENVIRONMENT_ID`と`ANTHROPIC_ENVIRONMENT_KEY`を使って、self-hosted environmentのwork queueを監視します。

#### 4. Sessionを作成する

```bash
uv run python create_session.py
```

`create_agent.py`と`create_environment.py`で作成したIDを使ってsessionを作成し、`.output/create_session.json`に保存します。

#### 5. Agentを呼ぶ

```bash
uv run python call_agent.py
```

`user.message`をsessionに送信し、応答イベントをストリームします。`call_agent.py`の`message`を変えると、実行内容を簡単に変えられます。

### 補足

- `call_agent.py`は`.output/create_session.json`を読み込みます。
- `worker.py`は`workspace/`ディレクトリを作業ディレクトリとして使います。

### 参考

- [Claude Managed Agents quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart)
- [Define your agent](https://platform.claude.com/docs/en/managed-agents/agent-setup)
- [Self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)
- [Start a session](https://platform.claude.com/docs/en/managed-agents/sessions)
- [Session event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)
- [Environment work queue](https://platform.claude.com/docs/en/api/beta/environments/work/poll)
- [llms.txt](https://platform.claude.com/llms.txt)

## English

### Prerequisites

- Python 3.13
- `uv`
- `ANTHROPIC_API_KEY`
- `ANTHROPIC_ENVIRONMENT_ID`
- `ANTHROPIC_ENVIRONMENT_KEY`

Copy `.env.sample` to `.env` and set the required values.

### Usage

This project runs in the following order:

1. Create the Agent
2. Create the Environment
3. Start the Worker
4. Create the Session
5. Call the Agent

#### 1. Create the Agent

```bash
uv run python create_agent.py
```

The Agent configuration is saved to `.output/create_agent.json`.

#### 2. Create the Environment

```bash
uv run python create_environment.py
```

The Environment configuration is saved to `.output/create_environment.json`.

Check the environment created in Claude Console and generate the environment key.

#### 3. Start the Worker

Set the following environment variables:

- `ANTHROPIC_ENVIRONMENT_ID`
- `ANTHROPIC_ENVIRONMENT_KEY`

```bash
uv run python worker.py
```

Keep the Worker running in a separate terminal or process. It monitors the self-hosted environment work queue using `ANTHROPIC_ENVIRONMENT_ID` and `ANTHROPIC_ENVIRONMENT_KEY`.

#### 4. Create the Session

```bash
uv run python create_session.py
```

Use the IDs created by `create_agent.py` and `create_environment.py` to create the session, then save it to `.output/create_session.json`.

#### 5. Call the Agent

```bash
uv run python call_agent.py
```

Send a `user.message` to the session and stream the response events. You can change the `message` in `call_agent.py` to adjust what gets executed.

### Notes

- `call_agent.py` reads `.output/create_session.json`.
- `worker.py` uses the `workspace/` directory as its working directory.

### References

- [Claude Managed Agents quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart)
- [Define your agent](https://platform.claude.com/docs/en/managed-agents/agent-setup)
- [Self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)
- [Start a session](https://platform.claude.com/docs/en/managed-agents/sessions)
- [Session event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)
- [Environment work queue](https://platform.claude.com/docs/en/api/beta/environments/work/poll)
- [llms.txt](https://platform.claude.com/llms.txt)
