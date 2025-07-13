
# PromptCue

PromptCue is a lightweight and extensible LLM API playground built using Streamlit and OpenRouter. It supports multiple open-source models such as Mistral and Mixtral, allowing users to send prompts, select models, and view responses along with latency and token usage statistics.

---

## Features

- Supports multiple models (Mistral-7B, Mixtral-8x7B)
- Minimal and attractive Streamlit UI
- Prompt-response interaction via OpenRouter
- Logs latency and token count per prompt
- Saves logs to both CSV and JSON
- Modular and beginner-friendly Python code

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/llm-api-playground.git
cd llm-api-playground
````

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

* Windows:

```bash
venv\Scripts\activate
```

* macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Add your OpenRouter API key

Create a `.env` file in the root directory:

```env
OPENROUTER_API_KEY=your-api-key-here
```

Or copy from `.env.example`.

### 5. Run the Streamlit App

```bash
streamlit run app.py
```

---

## Running Tests

Run the simple test script to verify model integration:

```bash
python test/test_model.py
```

---

## Logs

Logs are saved in the `logs/` folder:

* `log.csv`: structured table of prompt interactions
* `log.json`: list of JSON entries with prompt metadata

Each log includes:

* Timestamp
* Prompt text
* Selected model
* Latency (seconds)
* Token count

---


## Example Sample Logs

**log.csv**:

```csv
timestamp,prompt,model,latency_sec,token_count
2025-07-13T23:21:47.429262,What is AI?,mistral,3.226,92
2025-07-13T23:26:30.964042,Who are BTS?,mixtral,4.841,170
````

**log.json**:

```json
[
  {
    "timestamp": "2025-07-13T23:21:47.429262",
    "prompt": "What is AI?",
    "model": "mistral",
    "latency_sec": 3.226,
    "token_count": 92
  },
  {
    "timestamp": "2025-07-13T23:26:30.964042",
    "prompt": "Who are BTS?",
    "model": "mixtral",
    "latency_sec": 4.841,
    "token_count": 170
  }
]
```

