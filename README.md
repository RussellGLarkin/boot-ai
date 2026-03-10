# boot-ai 🤖

A custom-built AI Agent capable of interacting with the local file system and executing Python code. This project was developed as part of the **Build an AI Agent in Python** module on [Boot.dev](https://www.boot.dev).

The agent uses **Google Gemini** as its "brain" and is equipped with a suite of custom Python tools to bridge the gap between LLM reasoning and local system execution.



---

## 🛠️ Features

* **Autonomous Task Execution:** Uses Gemini's function-calling capabilities to choose the right tool for a given prompt.
* **File System Operations:** Read, write, and manage local files programmatically (see `functions/`).
* **Dynamic Code Execution:** A built-in tool to run Python scripts on the fly and capture output.
* **Modern Tooling:** Managed with `uv` for lightning-fast dependency management and reproducible environments.

---

## 🏗️ Project Structure

The project is organized into modular tools and a robust test suite:

* `main.py`: The entry point for the AI agent loop.
* `functions/`: Logic for the agent's core tools (get_files, get_file_content, write_files).
* `calculator/`: A command-line calculator app that the AI agent can work on.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.11+
* [uv](https://github.com/astral-sh/uv) installed
* A Google Gemini API Key

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/RussellGLarkin/boot-ai.git](https://github.com/RussellGLarkin/boot-ai.git)
   cd boot-ai

2. **Install dependencies:**
   ```bash
   uv sync

3. **Configure environment:**
   Ensure your Gemini API key is accessible via a .env file



