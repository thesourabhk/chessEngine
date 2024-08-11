# ChessEngine

A comprehensive Chess Engine built in Python. This engine is designed to simulate a complete chess game, providing move generation, handling special chess rules like castling, en passant, and pawn promotion, and supporting advanced features like move undo and check/checkmate detection.

## Features

- **Full Chess Game Simulation**: Supports the entire range of standard chess moves.
- **Move Generation**: Generates all legal moves for the current board state.
- **Check and Checkmate Detection**: Accurately detects check and checkmate conditions.
- **Castling, En Passant, and Pawn Promotion**: Fully implements these special chess rules.
- **Undo Moves**: Ability to undo the last move, with full restoration of the previous game state.
- **Pin and Check Detection**: Identifies pieces that are pinned and checks that are currently active.
- **Flexible Input/Output**: Supports both GUI and console-based interfaces.

## Installation

To use the ChessEngine, clone this repository and ensure you have Python 3 installed on your machine.

```bash
git clone https://github.com/thesourabhk/ChessEngine.git
cd ChessEngine
pip install -r requirements.txt
python ChessMain.py
```
