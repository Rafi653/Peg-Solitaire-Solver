"""Core solver (DFS-based) for Peg Solitaire."""

from typing import List, Optional
from board_manager import Board, initialize_board_configuration


def dfs_peg(root: Board, best_score_ref: List[int], best_path_ref: List[List[int]], path: List[int] = []) -> Optional[List[int]]:
    # update best known partial solution (min remaining pegs)
    if root.score() < best_score_ref[0]:
        best_score_ref[0] = root.score()
        best_path_ref[0] = path

    root.generate_children()

    if root.score() == 1:
        return path

    branch = 0
    for child in root.get_children():
        child_result = dfs_peg(child, best_score_ref, best_path_ref, path + [branch])
        if child_result:
            return child_result
        branch += 1
    return None


def print_winning_moves(root: Board, child_choices: List[int]) -> None:
    for child_idx in child_choices:
        root = root.get_children()[child_idx]
        print(child_idx)


def get_winning_moves(root: Board, child_choices: List[int]) -> List[tuple]:
    moves = []
    for child_idx in child_choices:
        root = root.get_children()[child_idx]
        moves.append(root.move)
    return moves


def solve_board(initial_empty: List[int]):
    """Solve the board and return the list of moves (from,skip,to) or [] if none."""
    initial_config = initialize_board_configuration(initial_empty)
    board = Board(initial_config)
    best_score = [len(initial_config)]
    best_performance: List[List[int]] = [[]]

    move_chain = dfs_peg(board, best_score, best_performance)

    if move_chain:
        return get_winning_moves(board, move_chain)
    return get_winning_moves(board, best_performance[0])
