"""Command-line entrypoint for running the solver and producing an animated GIF.

Example:
    python solver.py --initial-empty "0 3" --height 5 --output output.gif
"""

from pathlib import Path
import argparse
import imageio
import network_manager as nm
from peg_solver import solve_board
from network_manager import generate_winning_graphic
from board_manager import initialize_board_configuration


def _parse_initial_empty(raw: str):
    if not raw:
        return []
    # accept space- or comma-separated lists
    raw = raw.replace(',', ' ')
    return [int(x) for x in raw.split() if x.strip()]


def main():
    parser = argparse.ArgumentParser(description='Peg Solitaire solver')
    parser.add_argument('--initial-empty', '-e', help='Initial empty node indices (e.g. "0 3" or "0,3")')
    parser.add_argument('--height', '-H', type=int, help='Triangular board height (default from config)')
    parser.add_argument('--output', '-o', default='output.gif', help='Output GIF filename')

    args = parser.parse_args()

    if args.height:
        nm.set_height(args.height)

    if args.initial_empty:
        initial_empty = _parse_initial_empty(args.initial_empty)
    else:
        raw = input('Please input initial empty nodes (space separated): ')
        initial_empty = _parse_initial_empty(raw)

    init = initialize_board_configuration(initial_empty)
    moves = solve_board(initial_empty)

    if not moves:
        print('No solution found or solver returned no moves.')
        return

    output_path = Path.cwd().joinpath('Frames')
    output_path.mkdir(parents=True, exist_ok=True)

    generate_winning_graphic(moves, init)

    file_list = sorted(output_path.glob('*.png'))
    frames = []
    for file in file_list:
        print(file)
        frames.append(imageio.imread(file))

    if not frames:
        print('No frames were generated — aborting GIF creation.')
        return

    imageio.mimsave(args.output, frames, duration=0.75)
    print(f'Wrote {args.output} ({len(frames)} frames)')


if __name__ == '__main__':
    main()