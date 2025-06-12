# AI-Coding-Agent
AI Agent to generate and modify full-stack web apps using natural language prompts.

# 🧠 Terminal AI Dev Agent

An AI agent that creates, modifies, and manages full-stack web applications using natural language prompts. It understands folder structure, writes frontend/backend code, installs dependencies, and supports iterative development — all from your terminal.

---

## 🚀 Features

- 🧾 Understands natural language prompts
- 📂 Creates complete folder and file structures
- 🧠 Uses chain-of-thought and multi-shot prompting
- 🧱 Writes real code into appropriate files (React, Python, etc.)
- 🔁 Supports multi-turn interaction and follow-up prompts
- 🎨 Asks for themes, color preferences, and tech stack if ambiguous
- 🛠️ Executes shell commands like `npm install`, `vite`, `pip install`
- 💬 Maintains context using an array of messages

---

## 📦 How It Works

The agent follows a structured 4-step loop:

1. **Analyze** – Understands the user’s prompt and clarifies any ambiguity.
2. **Plan** – Outlines what files and commands are needed.
3. **Execute** – Creates files, writes code, and runs commands.
4. **Finish** – Describes what was done and asks for the next feature.

Each step is output as structured JSON for easy processing.

---

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.
