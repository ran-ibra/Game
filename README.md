# Game Agents Backend – Phase 1 (Trial)

This repository contains the **Phase 1 trial implementation** of the multi-agent backend layer for the RTS game.

The goal of this phase is to prove the ability to:

1. Design a **non-trivial world schema** (continent → regions → cities → resources → factions…).
2. Build a **clean, extensible FastAPI backend**.
3. Implement three core agents:
   - `WorldDesigner`
   - `ContentBuilder`
   - `EventsAgent`
4. Implement a simple but working `NarrativeController`.
5. Expose two working endpoints:
   - `POST /generate_world`
   - `POST /propose_events`
6. Add a minimal **Snapshot + Versioning** layer.
7. Provide clear documentation so the project can be run locally.

---

## 🔧 Tech Stack

- **Python** 3.10+
- **FastAPI**
- **Uvicorn** (ASGI server)
- **SQLAlchemy**
- **SQLite** with JSON columns (for the trial; easily upgradable to PostgreSQL)

---

## 🖥 How to Run Phase 1 on Your Machine

These steps assume a standard Python environment on Windows, macOS, or Linux.

### 1) Clone the repository

```bash
git clone https://github.com/ran-ibra/Game.git
cd Game
# in Game terminal
pip install -r requirements.txt
uvicorn app.main:app --reload
http://127.0.0.1:8000
#or
http://127.0.0.1:8000/docs

