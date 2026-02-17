# Peg Solitaire Solver

A Python-based solver for the classic Peg Solitaire puzzle game that uses graph-based algorithms to find solutions and visualize them through animated GIFs.

## Overview

This project provides an automated solution for solving Peg Solitaire puzzles. It uses a network-based approach to model the game board and employs algorithmic solving techniques to find valid move sequences that solve the puzzle.

## Project Structure

- **Solver.py** - Main entry point for solving Peg Solitaire puzzles. Generates `output.gif` visualization of the solution
- **board_manager.py** - Handles board state management, move validation, and board configuration
- **network_manager.py** - Manages the graph-based representation of the board and valid connections between positions
- **peg_solver.py** - Core solving algorithm implementation
- **for-if-you-want-to-test.ipynb** - Interactive Jupyter notebook for experimentation and testing (highly recommended for learning)
- **requirements.txt** - Python dependencies

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Rafi653/Peg-Solitaire-Solver.git
   cd Peg-Solitaire-Solver
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Solver

Execute the main solver script (supports CLI flags):
```bash
python solver.py --initial-empty "0 3" --height 5 --output output.gif
```

If `--initial-empty` is omitted the script will prompt interactively. Options:
- `--initial-empty`, `-e`: space- or comma-separated list of empty node indices
- `--height`, `-H`: triangular board height (small integer)
- `--output`, `-o`: output GIF filename (default: `output.gif`)

This will:
- Solve the Peg Solitaire puzzle
- Generate an animated GIF showing the solution steps (saved to `--output`)

### Interactive Testing

For experimentation and testing, use the Jupyter notebook:
```bash
jupyter notebook for-if-you-want-to-test.ipynb
```

This notebook allows you to:
- Test different board configurations
- Debug the solving algorithm
- Visualize intermediate steps
- Experiment with modifications

### Running tests

This project includes basic unit tests using `pytest`:
```bash
pip install -r requirements.txt
pytest -q
```

## How It Works

1. **Board Initialization** - The board state is set up with initial peg positions
2. **Network Modeling** - Valid position connections are modeled as a graph
3. **Algorithm** - The solver explores valid move sequences using backtracking/BFS
4. **Visualization** - The solution is rendered as an animated GIF showing each move

## Future Development Plans

### Phase 1: Enhanced Documentation & Testing
- [ ] Add comprehensive docstrings to all modules
- [ ] Create detailed algorithm explanation with diagrams
- [ ] Add unit tests for board validation and moves
- [ ] Document different board configurations

### Phase 2: Expand Board Game Support
- [ ] **Chinese Checkers Solver** - Implement multi-player game solving
- [ ] **Checkers/Draughts** - Full checkers game solver
- [ ] **Eight Puzzle Solver** - Add the classic 8-puzzle problem
- [ ] **Knights Tour** - Implement knight's tour problem solver

### Phase 3: Current Game Enhancements
- [ ] Support multiple Peg Solitaire variants (English, French, German boards)
- [ ] Implement difficulty levels and move optimization
- [ ] Add performance metrics and timing analysis
- [ ] Create interactive web interface for visualization
- [ ] Store and retrieve solution history
- [ ] Add move validation with detailed error messages

### Phase 4: General Framework
- [ ] Develop abstract base classes for board games
- [ ] Create a modular solver framework applicable to multiple games
- [ ] Implement common algorithms (BFS, DFS, A*, etc.)
- [ ] Performance optimization and benchmarking

## Architecture Vision

The project is evolving toward a **general game-solving framework** where:
- Each game inherits from a `BoardGame` base class
- Different solvers can be plugged in (BFS, DFS, Heuristic-based)
- Visualization is abstracted and reusable
- Board configurations are externalized and flexible

## Contributing

Contributions are welcome! Areas for improvement:
- Additional board game implementations
- Algorithm optimizations
- Better documentation
- Test coverage
- UI/visualization enhancements

## License

(To be added)

## Contact

For questions or suggestions, feel free to open an issue or discussion in this repository.