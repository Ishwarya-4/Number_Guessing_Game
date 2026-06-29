# 🔢 Number Guessing Game

A terminal-based Python game where you try to guess a randomly chosen number between 1 and 100. Pick your difficulty, use the "too high / too low" hints wisely, and see if you can crack it before your attempts run out.

---

## 🎮 How It Works

1. The game picks a random number between **1 and 100**
2. You choose a difficulty — **Easy** (10 attempts) or **Hard** (5 attempts)
3. After each guess, the game tells you if your guess was **too high**, **too low**, or **correct**
4. Guess correctly and you're offered a rematch; run out of attempts and the game ends
5. If you choose to play again, the screen clears and a fresh round begins with a new number

---

## 🗂️ Project Structure

```
Number_Guessing_Game/
├── main.py    # All game logic — difficulty selection, guessing loop, play-again flow
└── art.py     # ASCII art logo displayed at the start of each game
```

---

## 🎯 Difficulty Levels

| Level | Attempts |
|---|---|
| Easy | 10 |
| Hard | 5 |

---

## 🚀 Getting Started

**Prerequisites:** Python 3.x — no third-party libraries required.

```bash
git clone https://github.com/Ishwarya-4/Number_Guessing_Game.git
cd Number_Guessing_Game
python main.py
```

---

## 💡 Sample Gameplay

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Guess the number: 50
Too high.
You have 9 attempts remaining to guess the number.
Guess the number: 25
Too low.
...
```

---

## 🧠 Concepts Demonstrated

- **Recursive game loop** — `number_guessing_game()` calls itself when the player chooses to play again, cleanly restarting with a fresh number and difficulty
- **Function decomposition** — logic is split into focused functions: `compare_guess()`, `try_attempts()`, and `play_again()`
- **`random.randint()`** — generates a new secret number each round
- **Docstrings** — every function is documented with a clear description
