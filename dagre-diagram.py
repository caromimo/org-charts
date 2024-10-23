from dagre_py.core import plot

plot(
    {
        "nodes": [
            {"label": "Christine"},
            {"label": "Erin"},
            {"label": "Alex"},
            {"label": "Nasila"},
            {"label": "Ladan"},
            {"label": "Marie-Odile"},
            {"label": "Matt"},
            {"label": "Asma"},
            {"label": "Hocine"},
            {"label": "Ann"},
        ],
        "edges": [
            {"source": "Christine", "target": "Erin"},
            {"source": "Christine", "target": "Alex"},
            {"source": "Erin", "target": "Nasila"},
            {"source": "Erin", "target": "Ladan"},
            {"source": "Erin", "target": "Marie-Odile"},
            {"source": "Erin", "target": "Matt"},
            {"source": "Alex", "target": "Asma"},
            {"source": "Alex", "target": "Hocine"},
            {"source": "Alex", "target": "Ann"},
        ],
    }
)
