# LiveKit Agent Demo

This project implements a LiveKit voice agent using Azure for STT/TTS and OpenAI for LLM.

## Prerequisites

- Python 3.9+
- Azure Speech Services account
- OpenAI API account

## Setup

1.  **Clone the repository** (if applicable)

2.  **Create and activate a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration**:
    - Copy the example environment file:
      ```bash
      cp .env.example .env
      ```
    - Edit `.env` and fill in your API keys
    - Customize prompts in `prompts.yaml` if required.

## Running the Agent

download necessary files and start the agent only once:
```bash
python agent.py downlaod-files
```

Start the agent:
```bash
python agent.py start
```