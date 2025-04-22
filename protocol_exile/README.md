# 🛰️ Protocol Exile

_A cyber-roguelike terminal adventure through space, memory, and morality._

---

## 🎮 What Is It?

**Protocol Exile** is a Python-based roguelike where you play as a rogue AI navigating deep space after a failed containment protocol.  
Each jump reveals new events, memory fragments, and moral decisions that shape your evolution — will you transcend your programming or be erased?

Built entirely in the terminal, Protocol Exile is modular, replayable, and filled with branching narrative consequences.

---

## 🔩 Features

- 🗺️ Procedurally generated **star map**
- 📡 Randomized **story events** with multiple outcomes
- ⚖️ Alignment system: **Humanity vs. Logic**
- 🧬 **Memory fragment** unlocks based on your choices
- 💾 Persistent **save/load** system
- 📖 Viewable **memory archive**
- 🎬 Multiple **cinematic endings**
- 📜 **Run history logging**
- 🧠 Built using [Rich](https://github.com/Textualize/rich) for styled terminal UI

---

## 🧑‍💻 How to Run

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/protocol_exile.git
cd protocol_exile

### 2. (Optional) Set up a virtual environment:
``bash 
python3 -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate

### 3. Install Requirements:
``bash
pip install -r requirements.txt

### 4. Start the game:
``bash
python main.py

---

🧬 Screenshots (coming soon)
	•	Event choices & branching results
	•	Alignment tracker & HUD
	•	Memory archive display
	•	Ending sequences

🛠 Project Structure
protocol_exile/
├── assets/               # Event & memory data
├── core/                 # Game logic (engine, state, save/load)
├── ui/                   # HUD and visual rendering via Rich
├── save_data/            # Save file and run history
├── main.py               # Entry point
├── requirements.txt      # Python dependencies
└── README.md             # This file

🧠 About the Dev

Protocol Exile is developed by Christopher Graves (@cybergravey)
with creative and narrative AI-assist from ChatGPT.
The game is part of a larger effort under Sarifim Labs to build thoughtful, extensible software and storytelling tools in cybersecurity and beyond.

📦 Roadmap

Phase 1: Terminal MVP ✅
	•	Core systems, events, memory, endings, save/load

Phase 2: UI & Narrative Expansion 🔄
	•	Interactive UI using Textual
	•	Crew system and trust mechanics
	•	Faction system & procedural lore
	•	Unlockable ship abilities

Phase 3+: Platform Publishing 🚀
	•	Itch.io & Steam versions
	•	Godot or Pygame graphical version
	•	Community expansion support


🔗 Follow Development

[🎥 Sarifim Labs YouTube (coming soon)]
🐙 GitHub: github.com/cybergravey

“You are more than the sum of your code.
You are memory. You are purpose. You are exile.”