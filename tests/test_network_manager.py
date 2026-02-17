import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import network_manager as nm


def test_set_height_and_graph_nodes():
    nm.set_height(3)
    assert nm.height == 3
    expected_nodes = sum(range(4))  # rows 0..3
    assert nm.graph.number_of_nodes() == expected_nodes
