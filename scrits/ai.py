#!/usr/bin/env python3
import ollama
import sys
import json
import os
from rich.console import Console
from rich.markdown import Markdown, Heading
from rich.live import Live
from rich.style import Style
from rich.text import Text

MODEL = "qwen2.5-coder:14b"
HISTORY_FILE = os.path.expanduser("~/.config/fish/scrits/.ai_history.json")

HEADING_STYLES = {
    "h1": Style(color="#7aa2f7", bold=True),
    "h2": Style(color="#7aa2f7", bold=True),
    "h3": Style(color="#bb9af7", bold=True),
    "h4": Style(color="#bb9af7", bold=True),
    "h5": Style(color="#2ac3de", bold=True),
    "h6": Style(color="#2ac3de", bold=True),
}

def patched_heading(self, console, options):
    text = self.text.copy()
    text.justify = self.LEVEL_ALIGN.get(self.tag, "left")
    style = HEADING_STYLES.get(self.tag, Style(bold=True))
    text.stylize(style)
    yield text

Heading.__rich_console__ = patched_heading

console = Console()

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE) as f:
            return json.load(f)
    return []

def save_history(messages):
    with open(HISTORY_FILE, "w") as f:
        json.dump(messages, f)

messages = load_history()
user_input = " ".join(sys.argv[1:])
messages.append({"role": "user", "content": user_input})

response = ollama.chat(model=MODEL, messages=messages, stream=True)

full = ""
with Live(console=console, refresh_per_second=10) as live:
    for chunk in response:
        full += chunk["message"]["content"]
        live.update(Markdown(full, code_theme="one-dark"))

messages.append({"role": "assistant", "content": full})
save_history(messages)
