# Basic Poker Probability Engine

A lightweight, terminal-based Python application that calculates the probability of winning, tying, or losing in a Texas Hold'em poker game against a single random opponent.

## Features

- Evaluates hand odds given 2 hole cards and any known community cards (0, 3, 4, or 5 cards).
- Provides exact probabilities through combinatorial enumeration for post-flop scenarios.
- Approximates pre-flop probabilities using a Monte Carlo simulation (to avoid excessive computation time).
- Accurate 7-card poker hand evaluator ranking all standard Texas Hold'em hands.
- Pure Python implementation with no external poker dependencies.

## Setup Instructions

1. Ensure you have Python 3 installed. No external packages are required as it uses only the standard library.
2. Clone this repository or download the source code.
3. Open a terminal and navigate to the project directory.

## Usage

Run the main engine script:
```bash
python main.py
```

The application will prompt you for:
1. **Your hole cards**: Enter two cards separated by a space (e.g., `As Kh` for Ace of Spades and King of Hearts). Valid suits are `s` (spades), `h` (hearts), `d` (diamonds), `c` (clubs). Valid ranks are `2-9`, `T`, `J`, `Q`, `K`, `A`.
2. **Community cards**: Enter any known community cards separated by a space (e.g., `Ts Jd Qc`), or press Enter if it is pre-flop.

### Example Run
```text
Enter your 2 hole cards (e.g., 'As Kh' for Ace of Spades, King of Hearts): As Ah
Enter known community cards, separated by space (press Enter if pre-flop): Ks Qs Js

------------------------------------------------------------
Player Hand:     As Ah
Community Cards: Ks Qs Js

Calculating probabilities... Please wait.
------------------------------------------------------------
Results:
Method Used:     Exact Combinatorial Enumeration
Total Scenarios: 1,070,190
Wins:            728,953 (68.11%)
Ties:            31,659 (2.96%)
Losses:          309,578 (28.93%)
------------------------------------------------------------
```

## Mathematical Approach

- **Pre-Flop (0 community cards)**: An exact evaluation of all combinations pre-flop requires checking over 2 billion hands. To ensure the script remains responsive, a Monte Carlo simulation (50,000 random iterations) is used for pre-flop calculations to quickly approximate the true odds.
- **Post-Flop (3, 4, or 5 community cards)**: The engine uses exact combinatorial enumeration. It exhaustively iterates through every possible remaining community card and all possible opponent hole cards to calculate the exact win, tie, and loss ratios deterministically.
