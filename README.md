# VANTIS

### **Voice-Activated Neural Task & Interaction System**

> **A personalized voice-controlled computer agent designed to understand, reason, and perform tasks directly on your computer.**

VANTIS is an intelligent desktop computer agent designed to make human-computer interaction more natural through **voice commands**.

Instead of manually navigating through applications, folders, settings, and system controls, users can communicate with their computer using natural language.

VANTIS is designed to go beyond a traditional voice assistant. It will be capable of **understanding commands, executing computer operations, interacting with applications, controlling system settings, handling files, providing contextual feedback, and safely requesting confirmation before performing potentially destructive operations.**

---

## 🚀 Vision

The goal of VANTIS is to create a personalized AI layer between the user and their computer.

Instead of:

```text
User → Mouse / Keyboard → Application
```

VANTIS aims to provide:

```text
User
  ↓
Voice Command
  ↓
Speech Recognition
  ↓
Command Understanding
  ↓
Reasoning & Intent Detection
  ↓
Safety Verification
  ↓
Task Execution
  ↓
Computer
```

The long-term goal is to make common computer interactions possible through simple natural-language instructions.

For example:

> **"Open Chrome."**

> **"Set the volume at 50 percent."**

> **"Open my DSA folder."**

> **"Close WhatsApp."**

> **"Type my assignment title."**

> **"Scroll down."**

And for potentially dangerous operations:

> **"Delete this folder."**

VANTIS should recognize that the operation is destructive and respond:

> **"This will permanently delete the folder. Should I continue?"**

The action should only be performed after explicit confirmation.

---

# ✨ Features

## 🎙️ Voice Control

VANTIS uses voice as its primary interaction method.

The system captures the user's speech, converts it into text, identifies the requested action, and executes the corresponding operation.

Example:

```text
User: Open Chrome

VANTIS:
Opening Chrome.
```

---

## 🖥️ Application Control

VANTIS is designed to launch and close desktop applications through voice commands.

Examples:

```text
Open Chrome
Open VS Code
Open WhatsApp
Open Settings
Open Calculator
Close Chrome
Close VS Code
Close WhatsApp
```

The application controller can map user-friendly names to the actual Windows applications and processes.

---

## ⌨️ Keyboard Automation

VANTIS can interact with the keyboard programmatically.

Supported operations include:

```text
Press Enter
Press Escape
Press Tab
Type Hello World
```

It can also perform keyboard shortcuts:

```text
Copy it
Paste it
Cut it
Undo
Redo
Select all
```

---

## 🖱️ Mouse Automation

VANTIS can control the mouse to perform common interactions.

Examples:

```text
Click
Double click
Right click
Scroll up
Scroll down
```

The system is designed so that these low-risk interactions can happen silently without unnecessary voice feedback.

---

## 🔊 System Volume Control

VANTIS provides direct control over the Windows master volume.

Supported commands:

```text
Set volume at 50
Set volume at 75 percent
Mute
Unmute
```

The system can directly set the volume to a requested percentage rather than repeatedly pressing volume-up or volume-down keys.

---

## ☀️ Brightness Control

VANTIS is designed to provide voice-based display brightness control.

Examples:

```text
Set brightness at 50 percent
Set brightness at 80 percent
```

Brightness control will be integrated into the system-control layer.

---

## 📁 File & Folder Operations

VANTIS is designed to interact with files and folders using natural-language commands.

Potential operations include:

```text
Open my DSA folder
Create a folder
Rename this file
Move this file
Delete this file
```

File operations will be handled through a dedicated file-management layer rather than mixing filesystem logic with the command parser.

---

# 🛡️ Safety & Confirmation System

One of the most important design goals of VANTIS is **safe computer automation**.

Not every command should be executed immediately.

### Low-risk commands

Commands such as:

```text
Click
Scroll down
Press Enter
Open Chrome
Set volume at 50
```

can be executed directly.

For these commands, VANTIS can remain silent or provide a short completion message depending on the action.

### Dangerous commands

Potentially destructive commands should require explicit confirmation.

Examples:

```text
Delete a file
Delete a folder
Format a drive
Shutdown the computer
Restart the computer
Terminate critical processes
```

Instead of immediately executing:

```text
Delete this folder
```

VANTIS should respond:

```text
This will permanently delete the folder.
Should I continue?
```

Only after receiving a valid confirmation such as:

```text
Yes
Confirm
Proceed
```

should the operation be executed.

This safety layer is intended to prevent accidental destructive actions caused by:

* Speech-recognition errors
* Misunderstood commands
* Accidental voice input
* Ambiguous instructions
* Incorrect application identification

---

# 🔈 Intelligent Voice Feedback

VANTIS is designed to distinguish between actions that require a response and actions that do not.

### Silent actions

Simple interactions should not unnecessarily interrupt the user.

```text
Scroll down
Click
Double click
Press Enter
```

No spoken response is required.

### Spoken responses

VANTIS should provide feedback for:

* Errors
* Important confirmations
* Task completion
* Application operations
* Potentially dangerous actions

Example:

```text
User:
Open Chrome.

VANTIS:
Opening Chrome.
```

Another example:

```text
User:
Delete this file.

VANTIS:
This will permanently delete the file.
Should I continue?
```

This creates a more natural interaction instead of making VANTIS speak after every mouse or keyboard action.

---

# 🧠 Intelligent Command Processing

The command-processing system is designed around a layered architecture.

```text
Voice Input
     ↓
Speech Recognition
     ↓
Command Parser
     ↓
Intent Detection
     ↓
Action Generation
     ↓
Safety Check
     ↓
Command Executor
     ↓
Controller
     ↓
Operating System
```

Each component has a specific responsibility.

### Voice Controller

Responsible for:

* Microphone input
* Ambient-noise calibration
* Speech capture
* Speech-to-text conversion

### Command Parser

Responsible for:

* Understanding recognized commands
* Identifying command types
* Extracting parameters
* Generating structured actions

Example:

```text
"Set volume at 70 percent"
```

becomes:

```python
{
    "action": "set_volume",
    "amount": 70
}
```

### Command Executor

Responsible for:

* Receiving structured actions
* Selecting the appropriate controller
* Executing the requested operation
* Triggering feedback when necessary

### Controllers

Individual controllers isolate computer operations into separate modules.

Examples:

```text
KeyboardController
MouseController
ScreenController
ApplicationController
SystemController
VoiceController
```

This modular architecture makes VANTIS easier to expand and maintain.

---

# 🏗️ Architecture

The project follows a modular controller-based architecture.

```text
                    ┌───────────────┐
                    │     User      │
                    └───────┬───────┘
                            │
                         Voice
                            ↓
                  ┌──────────────────┐
                  │ Voice Controller │
                  └────────┬─────────┘
                           │
                      Speech → Text
                           ↓
                  ┌──────────────────┐
                  │ Command Parser   │
                  └────────┬─────────┘
                           │
                    Structured Action
                           ↓
                  ┌──────────────────┐
                  │ Safety / Intent  │
                  │     Layer        │
                  └────────┬─────────┘
                           │
                           ↓
                  ┌──────────────────┐
                  │ Command Executor │
                  └────────┬─────────┘
                           │
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
      Keyboard          Mouse          Application
      Controller       Controller       Controller
          │                │                │
          └────────────────┼────────────────┘
                           ↓
                    System Controller
                           ↓
                      Windows PC
```

---

# 🛠️ Tech Stack

## Programming Language

* **Python**

## Voice & Speech

* **SpeechRecognition**
* **Google Speech Recognition**
* **PyAudio**

## Text-to-Speech

* **pyttsx3**

## Computer Automation

* **PyAutoGUI**

Used for:

* Mouse control
* Keyboard control
* Scrolling
* Keyboard shortcuts
* Basic system interactions

## Windows System Control

* **pycaw**
* **COM / comtypes**

Used for:

* Master volume control
* Mute / unmute
* Other Windows-level system functionality

## Process Management

* **psutil**

Used for:

* Detecting running applications
* Identifying application processes
* Closing applications safely

## Application Launching

* **subprocess**
* **Windows command-line utilities**

Used for:

* Opening applications
* Opening folders
* Launching URLs
* Interacting with Windows applications

## Development Environment

* **Visual Studio Code**
* **Python Virtual Environment (`venv`)**
* **Git**
* **GitHub**

---

# 📦 Installation

## 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd VANTIS
```

---

## 2. Create a virtual environment

```bash
python -m venv venv
```

---

## 3. Activate the virtual environment

### Windows PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### Windows Command Prompt

```cmd
venv\Scripts\activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

If dependencies have not yet been added to `requirements.txt`, install the core packages manually:

```bash
pip install SpeechRecognition
pip install PyAudio
pip install pyautogui
pip install psutil
pip install pycaw
pip install comtypes
pip install pyttsx3
```

---

# ▶️ Running VANTIS

Activate the virtual environment first:

```powershell
venv\Scripts\Activate.ps1
```

Then start VANTIS:

```bash
python main.py
```

VANTIS will initialize the microphone and begin listening for commands.

Example:

```text
Microphone ready.
Listening...
Recognizing...

You said: open chrome

Opening Chrome.
```

---

# 🔄 Restarting VANTIS

Instead of manually stopping and starting the program, VANTIS supports a restart command.

Say:

```text
Restart Jarvis
```

The application restarts itself using the existing Python process.

The command will eventually be renamed to match the final VANTIS identity:

```text
Restart VANTIS
```

---

# 📂 Project Structure

The project is organized into independent controllers and processing layers.

```text
VANTIS/
│
├── controllers/
│   ├── application_controller.py
│   ├── keyboard_controller.py
│   ├── mouse_controller.py
│   ├── screen_controller.py
│   ├── system_controller.py
│   ├── voice_controller.py
│   ├── tts_controller.py
│   └── voice_feedback.py
│
├── command_parser.py
├── executor.py
├── main.py
├── requirements.txt
├── README.md
└── venv/
```

### `main.py`

The main entry point of the application.

Responsible for:

* Initializing controllers
* Starting the voice-processing loop
* Receiving voice commands
* Passing commands to the parser
* Sending actions to the executor

### `command_parser.py`

Converts natural-language commands into structured actions.

### `executor.py`

Executes the structured actions using the appropriate controller.

### `controllers/`

Contains the individual computer-control modules.

This separation prevents the entire project from becoming one large Python file.

---

# 🧪 Example Commands

## Applications

```text
Open Chrome
Open VS Code
Open WhatsApp
Open Settings

Close Chrome
Close VS Code
Close WhatsApp
```

## Mouse

```text
Click
Double click
Right click
Scroll up
Scroll down
```

## Keyboard

```text
Press Enter
Press Escape
Type Hello World
```

## Shortcuts

```text
Copy it
Paste it
Cut it
Undo
Redo
Select all
```

## System

```text
Set volume at 50 percent
Set volume at 80
Mute
Unmute

Set brightness at 60 percent
```

## Jarvis/VANTIS

```text
Restart VANTIS
Stop VANTIS
```

---

# 🗺️ Development Roadmap

VANTIS is being developed in multiple stages.

## Phase 1 — Computer Control

* [x] Keyboard controller
* [x] Mouse controller
* [x] Screen controller
* [x] Application controller
* [x] Basic system controller

## Phase 2 — Voice Interaction

* [x] Microphone integration
* [x] Speech recognition
* [x] Command parser
* [x] Command executor
* [x] Basic voice commands
* [x] Application control through voice
* [x] Keyboard control through voice
* [x] Mouse control through voice
* [x] System volume control

## Phase 3 — Intelligent Interaction

* [ ] Structured intent system
* [ ] Better natural-language understanding
* [ ] Context-aware commands
* [ ] Improved command recognition
* [ ] Command aliases
* [ ] Better error handling
* [ ] Intelligent task completion responses
* [ ] Consistent voice feedback system

## Phase 4 — Safety System

* [ ] Dangerous-action detection
* [ ] Confirmation workflow
* [ ] Destructive-action protection
* [ ] Application/process safety checks
* [ ] Confirmation timeout
* [ ] Cancel/abort commands
* [ ] Safe execution policies

## Phase 5 — File & System Automation

* [ ] File creation
* [ ] File deletion
* [ ] File renaming
* [ ] File movement
* [ ] Folder management
* [ ] Advanced system controls
* [ ] Brightness control
* [ ] Process management
* [ ] System information commands

## Phase 6 — AI Reasoning

* [ ] AI-powered intent detection
* [ ] Natural-language task interpretation
* [ ] Multi-step task execution
* [ ] Context awareness
* [ ] Task planning
* [ ] Ambiguous-command handling
* [ ] Conversational interaction

For example:

> **"Open VS Code, go to my project folder, and start the application."**

Instead of treating this as one simple command, VANTIS could break it into:

```text
1. Open VS Code
2. Locate project folder
3. Open project
4. Start application
5. Report completion
```

---

# 🔮 Future Vision

The final goal is for VANTIS to become more than a collection of voice commands.

It should evolve into an **intelligent computer agent capable of understanding goals rather than only individual commands.**

For example:

> **"Prepare my workspace for DSA."**

VANTIS could eventually understand the user's intent and perform multiple operations:

```text
Open VS Code
      ↓
Open DSA project
      ↓
Open browser
      ↓
Open required resources
      ↓
Adjust volume
      ↓
Prepare workspace
      ↓
"Your DSA workspace is ready."
```

The same architecture can eventually support:

* Multi-step automation
* Context-aware interactions
* Personalized workflows
* AI-based reasoning
* Computer vision
* Screen understanding
* Application-specific automation
* Local AI models
* Natural conversational interaction
* Autonomous task execution with safety controls

---

# 🔐 Design Principles

VANTIS is built around several core principles.

### 1. Natural Interaction

Users should be able to communicate naturally instead of memorizing rigid commands.

### 2. Modular Architecture

Each capability should have its own controller or service.

### 3. Minimal Interruption

VANTIS should not speak unnecessarily.

Simple actions should happen silently.

### 4. Safety First

Potentially destructive operations should require explicit confirmation.

### 5. Extensibility

New capabilities should be addable without rewriting the entire application.

### 6. Personalization

VANTIS should eventually adapt to the user's applications, workflows, preferences, and frequently performed tasks.

---

# 🤝 Contributing

This project is currently being developed as a personal AI computer-agent project.

Ideas, improvements, bug reports, and feature suggestions are welcome as the project evolves.

---

# 📜 License

This project will be licensed under the license specified in the repository.

---

# 👨‍💻 Developer

**Priyanshu Thakur**

Computer Science & Engineering Student
Interested in:

* Artificial Intelligence
* Full-Stack Development
* Computer Automation
* Data Structures & Algorithms
* Software Engineering

---

# ⭐ VANTIS

**Voice-Activated Neural Task & Interaction System**

> *Personalized Voice-Controlled Computer Assistant*

VANTIS aims to bridge the gap between **human language and computer interaction**—turning spoken instructions into meaningful, safe, and executable computer actions.
