# resources: https://graphviz.readthedocs.io/en/stable/examples.html#hello-py
import graphviz


class Organization:
    def __init__(self):
        self.graph = graphviz.Graph(
            name="Orthogonal",
            graph_attr={"label": "MDCCD", "splines": "ortho"},
            node_attr={"shape": "box"},
        )

    def is_current_employee(row):
        if has_permanently_left(row):
            return False
        if is_on_temporary_leave(row):
            return False
        else:
            return True

    def add_staffing_action(self, row):
        self.graph.node(row["positionNumber"], label=f"{row["firstName"]} ")
        self.graph.edge(row["positionNumber"], row["reportsToPositionNumber"])
