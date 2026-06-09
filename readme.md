# 🐍 Snake Game

A classic Snake game built with **Python** and **pygame-ce**.

Eat food to grow longer, avoid crashing into yourself, and try to beat your high score!

---

## ✨ Features

- **Classic Snake Gameplay** — Smooth grid-based movement with arrow key controls
- **Score Tracking** — Live score counter displayed in a side panel
- **Best Score** — High score persists across rounds within a session
- **Wraparound Walls** — The snake wraps around the screen edges instead of dying
- **Instant Restart** — Automatically starts a new round on death — no menus, no waiting
- **UI Panel** — Clean stats sidebar showing current score and best score

---

## 🎮 Controls

| Key | Action |
| --- | ------ |
| `↑` | Move up |
| `↓` | Move down |
| `←` | Move left |
| `→` | Move right |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
- **pygame-ce**

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Escgot/Snake-Game.git
   cd Snake-Game
   ```

2. **Install dependencies**

   ```bash
   pip install pygame-ce
   ```

3. **Run the game**

   ```bash
   python snake.py
   ```

---

## 🖼️ How It Works

The game window is split into two areas:

- **Game Area** (600 × 400) — Where the snake moves and eats food
- **Stats Panel** (200 × 400) — Displays the current score and session best

When the snake collides with its own body, the round ends and a new one begins immediately. The high score carries over between rounds.

---

## 🛠️ Tech Stack

- **Python 3** — Core language
- **pygame-ce** — Rendering, input handling, and game loop

---

## 📄 License

This project is open source and available for personal use and learning.
