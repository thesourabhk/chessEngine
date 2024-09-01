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
```

## Usage

You can use the ChessEngine in two primary ways:

1. **Console Mode**

   Run the engine in console mode to play a game of chess directly in your terminal:

   ```bash
   python ChessMain.py

## GameState Class

The `GameState` class is the core of the engine. It maintains the board state, and move history, and handles move validation and execution.

- **Board Representation**: The board is an 8x8 2D list, where each element corresponds to a square on the chessboard.
- **Move History**: Keeps track of all moves made in the game, allowing for move undo functionality.
- **Check and Pin Detection**: The engine actively checks for checks and pins in the game state, ensuring all moves adhere to the rules of chess.
- **Special Moves**: Supports castling, en passant, and pawn promotion with proper validation.

## Move Generation

The engine uses an advanced move generation algorithm that considers all possible moves for a given game state. It accounts for special rules and efficiently generates legal moves.

### How It Works:

- **Normal Moves**: Calculates all possible normal moves (moving a piece to an empty square).
- **Capturing Moves**: Generates moves that capture an opponent's piece.
- **Special Moves**: Includes special moves like castling, en passant, and pawn promotion.
- **Move Validation**: Each generated move is validated to ensure it doesn't put the player in check.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - [sourabhd267@gmail.com](mailto:sourabhd267@gmail.com)

Project Link: [https://github.com/thesourabhk/ChessEngine](https://github.com/thesourabhk/ChessEngine)



