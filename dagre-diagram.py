from dagre_py.core import plot

plot(
    {
        "nodes": [
            {"label": "Christine"},
            {"label": "Lucie"},
            {"label": "Alex"},
            {"label": "Nasila"},
            {"label": "Ladan"},
            {"label": "Marie"},
            {"label": "Matt"},
            {"label": "Asma"},
            {"label": "Hocine"},
            {"label": "Ann"},
        ],
        "edges": [
            {"source": "Christine", "target": "Lucie"},
            {"source": "Christine", "target": "Alex"},
            {"source": "Lucie", "target": "Nasila"},
            {"source": "Lucie", "target": "Ladan"},
            {"source": "Lucie", "target": "Marie"},
            {"source": "Lucie", "target": "Matt"},
            {"source": "Alex", "target": "Asma"},
            {"source": "Alex", "target": "Hocine"},
            {"source": "Alex", "target": "Ann"},
        ],
    }
)
