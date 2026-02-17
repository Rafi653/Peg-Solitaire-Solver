
import network_manager as nm
from typing import Dict, List


def initialize_board_configuration(initial_empty: List[int]) -> Dict[int, str]:
    """Return a node->state mapping where nodes in `initial_empty` are 'empty'."""
    initial_config: Dict[int, str] = {}
    for row in range(nm.height + 1):
        for col in range(row):
            idx = sum(range(row)) + col
            initial_config[idx] = 'empty' if idx in initial_empty else 'filled'
    return initial_config


def get_empty(configuration: Dict[int, str]) -> List[int]:
    return [key for key, val in configuration.items() if val == 'empty']


class Board:
    """Tree node representing a board state and its possible next states."""

    def __init__(self, config: Dict[int, str], move=None):
        self.data = config
        self.children: List["Board"] = []
        self.move = move

    def get_possibles(self) -> Dict[int, str]:
        """Return a display-friendly map marking possible "moving" sources.

        This does not mutate the board; it returns a shallow copy annotated
        with 'moving' for filled nodes that can jump into an empty spot.
        """
        current_config = self.data.copy()
        for empty_node in get_empty(self.data):
            for neighbor in nm.graph.neighbors(empty_node):
                if self.data[neighbor] == 'filled':
                    for second_degree_neighbor in filter(lambda x: x != empty_node, nm.graph.neighbors(neighbor)):
                        edge1 = nm.graph.get_edge_data(neighbor, second_degree_neighbor)
                        edge2 = nm.graph.get_edge_data(neighbor, empty_node)
                        if edge1 and edge2 and edge1['typeof'] == edge2['typeof'] and self.data[second_degree_neighbor] == 'filled':
                            current_config.update({second_degree_neighbor: 'moving'})
                            break
        return current_config

    def generate_children(self) -> None:
        """Populate self.children with Board instances for all legal jumps."""
        for empty_node in get_empty(self.data):
            for neighbor in nm.graph.neighbors(empty_node):
                if self.data[neighbor] == 'filled':
                    for second_degree_neighbor in filter(lambda x: x != empty_node, nm.graph.neighbors(neighbor)):
                        edge1 = nm.graph.get_edge_data(neighbor, second_degree_neighbor)
                        edge2 = nm.graph.get_edge_data(neighbor, empty_node)
                        if edge1 and edge2 and edge1['typeof'] == edge2['typeof'] and self.data[second_degree_neighbor] == 'filled':
                            new_config = {**self.data, **{empty_node: 'filled', neighbor: 'empty', second_degree_neighbor: 'empty'}}
                            self.make_child(new_config, (second_degree_neighbor, neighbor, empty_node))
                            break

    def make_child(self, config: Dict[int, str], move=None) -> None:
        self.children.append(Board(config, move))

    def get_children(self) -> List["Board"]:
        return self.children

    def count_children(self) -> int:
        return len(self.children)

    def score(self) -> int:
        total_nodes = sum(range(nm.height + 1))
        return total_nodes - len(get_empty(self.data))

    def __str__(self) -> str:
        return str(self.data)