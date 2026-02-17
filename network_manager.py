"""Graph utilities for triangular Peg Solitaire.

This module exposes a mutable `height` and `graph` and allows regenerating
the board graph for different heights via `set_height(height)`.
"""

from pathlib import Path
import networkx as nx
import matplotlib.pyplot as plt

first_id_in_row = lambda row: sum(range(row+1))
graph_colors = {'empty': 'grey', 'filled': 'cyan', 'moving': 'orange', 'skipped': 'red'}

# module-level defaults (triangular board)
height = 5
graph: nx.Graph = nx.Graph()
graph_labels: dict = {}
positions: dict = {}


def _build_triangular_graph(h: int):
    g = nx.Graph()
    labels = {}
    pos = {}
    for row in range(h + 1):
        for col in range(row):
            idx = sum(range(row)) + col
            labels[idx] = str(idx)
            pos[idx] = ((col - (h + row) / 2) * 5, (h - row) * 5)
            g.add_node(idx)
            if col < row - 1:
                g.add_edge(idx, idx + 1, typeof='lateral')
            if row < h:
                g.add_edge(idx, idx + row, typeof='vertical_fwd')
                g.add_edge(idx, idx + row + 1, typeof='vertical_back')
    return g, labels, pos


def set_height(h: int):
    """Regenerate module-level graph/positions for a new triangular height.

    Calling `set_height` updates `height`, `graph`, `graph_labels` and
    `positions` in this module so other modules can read the new board.
    """
    global height, graph, graph_labels, positions
    height = int(h)
    graph, graph_labels, positions = _build_triangular_graph(height)


# initialize defaults
set_height(height)


def generate_winning_graphic(move_list, config, turn: int = 1):
    """Render move frames and save PNGs into ./Frames.

    - move_list: sequence of (from_node, skip_node, to_node) tuples
    - config: dict node->state (used for colors)
    """
    if not move_list:
        return

    Path('Frames').mkdir(parents=True, exist_ok=True)

    from_node, skip_node, to_node = move_list[0]

    # Phase 1: highlight origin
    config.update({from_node: 'moving'})
    nx.draw(graph, pos=positions, node_color=[graph_colors[config[node]] for node in graph.nodes()])
    plt.savefig(f'Frames/Turn {turn:02d} - Phase 1.png')
    plt.clf()

    # Phase 2: show jump in progress
    config.update({from_node: 'empty', skip_node: 'skipped', to_node: 'moving'})
    nx.draw(graph, pos=positions, node_color=[graph_colors[config[node]] for node in graph.nodes()])
    plt.savefig(f'Frames/Turn {turn:02d} - Phase 2.png')
    plt.clf()

    # Phase 3: finalize move
    config.update({skip_node: 'empty', to_node: 'filled'})
    nx.draw(graph, pos=positions, node_color=[graph_colors[config[node]] for node in graph.nodes()])
    plt.savefig(f'Frames/Turn {turn:02d} - Phase 3.png')
    plt.clf()

    print(f'turn {turn} done!')
    if len(move_list) > 1:
        generate_winning_graphic(move_list[1:], config, turn + 1)