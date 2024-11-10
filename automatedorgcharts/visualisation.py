import graphviz

# create a graph object
dot = graphviz.Digraph(comment="The Round Table")

# add nodes and edges
dot.node("A", "King Arthur")  # doctest: +NO_EXE
dot.node("B", "Sir Bedevere the Wise")
dot.node("L", "Sir Lancelot the Brave")

dot.edges(["AB", "AL"])
dot.edge("B", "L", constraint="false")

# check the source code
print(dot.source)

# save, render, and view
dot.render("doctest-output/round-table.gv", view=True)  # doctest: +SKIP
"doctest-output/round-table.gv.pdf"


d = graphviz.Digraph(
    name="Orthogonal",
    graph_attr={"label": "TEST", "splines": "ortho"},
    node_attr={"shape": "box"},
)

d.edges(["ab", "ac"])
d.edges(["bd", "be"])
d.edges(["cf", "cg", "ck"])

d.render("test.gv", view=True)
