import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import network_manager as nm
from peg_solver import solve_board


def test_solve_board_returns_list_for_small_board():
    nm.set_height(3)
    result = solve_board([0])
    assert isinstance(result, list)
