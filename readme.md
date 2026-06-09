# 🐍 Advanced Snake Game (Power-up Edition)

A feature-rich Snake game built with **Python** and **pygame-ce**.

Eat food to grow longer, survive using rare power-ups, and avoid crashing into yourself! The game features dynamic difficulty and a custom UI panel.

---

## ✨ Features

- **Classic Snake Gameplay** — Smooth grid-based movement with wraparound edges (no walls!).
- **Power-up System** — Rare items spawn randomly with unique effects:
    - 🍎 **Golden Apple**: Worth 5 points (disappears after 5s).
    - 🐌 **Slow Time**: Temporarily reduces game speed to help you survive.
    - ✂️ **Scissors**: Instantly cuts your snake's length in half.
- **Dynamic Difficulty** — The game speed increases as you progress.
- **Stats Panel** — Clean sidebar showing live score and session best.
- **Instant Restart** — Immediate respawn on death—no menus, no waiting.

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
   git clone [https://github.com/Escgot/Snake-Game.git](https://github.com/Escgot/Snake-Game.git)
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

Power-up Logic: Every few seconds, there is a small chance for a special item to spawn. If you miss it, it despawns after 5 seconds!

---

## 🛠️ Tech Stack

- **Python 3** — Core language
- **pygame-ce** — Rendering, input handling, and game loop

---

## 📄 License

This project is open source and available for personal use and learning.
