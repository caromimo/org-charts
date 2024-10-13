from dagre_py.core import plot

plot(
    {
        "nodes": [
            {"label": "A"},
            {"label": "B", "description": "This is an output node"},
        ],
        "edges": [
            {"source": "A", "target": "B", "label": "edge1"},
            {"source": "A", "target": "B", "label": "edge2"},
        ],
    }
)
