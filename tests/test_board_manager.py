import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import network_manager as nm
from board_manager import initialize_board_configuration, Board


def test_initialize_board_configuration_and_empty_nodes():
    nm.set_height(3)
    config = initialize_board_configuration([0, 2])
    assert len(config) == sum(range(nm.height + 1))
    assert config[0] == 'empty'
    assert config[2] == 'empty'
    assert all(v in ("empty", "filled") for v in config.values())


def test_generate_children_exists_for_some_positions():
    nm.set_height(4)
    total_nodes = sum(range(nm.height + 1))
    found = False
    for i in range(total_nodes):
        cfg = initialize_board_configuration([i])
        b = Board(cfg)
        b.generate_children()
        if b.count_children() > 0:
            found = True
            break
    assert found, "Expected at least one starting empty node to produce children"
