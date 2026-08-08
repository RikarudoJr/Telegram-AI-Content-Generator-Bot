# Project Setup: Task Understanding & Assignment Checklist

## Overview
- **Project Theme:** 4-Day Telegram Bot with OpenAI
- **Core Evaluation Focus:** Clean Technical Integration

---

## Assignment Checklist Table

| Key Question | Team / Project Understanding (4-Day Telegram Bot Sprint) |
| :--- | :--- |
| **1. What do you think the project is about?** | The project is about establishing a reliable integration pipeline between Telegram and OpenAI. To survive a 4-day timeline, the project is focused on **ruthless scoping**: locking in a single **Functional Archetype** (e.g., a multi-step data collector vs. a single-turn Q&A bot) on Day 1 and explicitly ignoring any features or complex interactions outside that archetype. |
| **2. What is the tutor/manager expecting you to do?** | • **System Design:** Scope down and finalize the single Functional Archetype on Day 1.<br>• **Clean Integration Tasks:** Secure API keys using `.env`, set up Telegram webhook connections, manage Telegram's timeout/retry logic to avoid duplicate responses, and write graceful error fallbacks when the OpenAI API fails. |
| **3. What does the assessment involve?** | • **Deliverable:** A live 5-minute demonstration of the Telegram bot on Day 4.<br>• **Key Check:** Ensure the "happy path" integration flow can be fully executed on a phone/screen within a tight 300-second window. |
| **4. What will the evaluator think is a 'good' project? (Assessment Criteria)** | The project will be judged on one core pillar:<br>1. **Clean Integration:** Robust, working connection handling API latency and errors gracefully. |

---

## 🗺️ Feature Map

| Status | Feature Name | User Action | Expected Result | Simplest Test |
| :---: | :--- | :--- | :--- | :--- |
| 🟢 | **Start Flow & Reset State** | Type `/start` and press send. | Bot clears previous session state, replies with welcome message, and prompts for **Step 1/2**: *"What topic would you like to write about?"* | Send `/start` in chat → Check if bot responds with Step 1 question. |
| 🟢 | **Collect Topic (Step 1)** | Type any topic text (e.g., `Time Management`). | Bot stores topic in `user_data["topic"]`, increments message count, and prompts for **Step 2/2**: *"What tone do you want to use?"* | Reply to Step 1 with `Time Management` → Check if bot asks for tone. |
| 🟡 *(OpenAI API integration remaining)* | **Collect Tone & Session Summary (Step 2)** | Type any tone text (e.g., `Professional`). | Bot stores tone, echos summary with topic & tone, displays session message count, and completes state flow (`ConversationHandler.END`). | Reply to Step 2 with `Professional` → Check if confirmation & message count are returned. |
| 🟢 | **Custom Reset Command** | Type `/reset` at any step. | Bot clears session state (`context.user_data.clear()`) and replies: *"session reset clean!"*. | Send `/start` then `/reset` → Check if bot confirms clean reset. |
| 🟢 | **Cancel Flow** | Type `/cancel` at any step. | Bot clears session state and confirms cancellation. | Send `/start` then `/cancel` → Check if bot confirms cancellation. |

---

## 🛠️ Project Structure

- `main.py` - Main entry point that initializes logging, loads handlers, and starts polling.
- `bot_handlers.py` - Conversation state machine handling user steps (`TOPIC`, `TONE`, `/start`, `/cancel`).
- `openai_service.py` - Asynchronous wrapper for calling OpenAI API without blocking the bot.
- `config.py` - Environment loader for Telegram and OpenAI secrets.
- `.env` / `.env.example` - Credentials file containing secrets (Git-ignored).
- `requirements.txt` - Python project dependencies.

---

## 🏁 Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Set up credentials** in `.env`:
   ```env
   TELEGRAM_BOT_TOKEN=your_token_here
   OPENAI_API_KEY=your_key_here
   ```
3. **Run the bot**:
   ```bash
   python main.py
   ```
