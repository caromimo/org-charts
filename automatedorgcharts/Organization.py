from datetime import date
from pprint import pp
import graphviz


class Organization:
    def __init__(self):
        self.employees = {}
        self.positions = {}

    def process_action(self, action):

        if action["action"] == "classification":

            if action["type"] == "create":
                self.positions[action["details"]["positionNumber"]] = action["details"]

            if action["type"] == "update":
                self.positions[action["details"]["positionNumber"]] = {
                    **self.positions[action["details"]["positionNumber"]],
                    **action["details"],
                }

            if action["type"] == "delete":
                del self.positions[action["details"]["positionNumber"]]

        if action["action"] == "staffing":

            if action["type"] in [
                "appointmentIN",
                "deploymentIN",
                "studentHiringOffer",
            ]:
                self.employees[action["details"]["employeePeopleSoftID"]] = action[
                    "details"
                ]
                # this can be cleaned later - adding the incumbent to the position
                self.positions[action["details"]["positionNumber"]] = {
                    **self.positions[action["details"]["positionNumber"]],
                    **{"incumbent": action["details"]["employeePeopleSoftID"]},
                }

            if action["type"] == "parentalLeave":
                if action["details"]["endDate"] > date.today():
                    del self.employees[action["details"]["employeePeopleSoftID"]]

            if action["type"] in ["deploymentOUT", "retirement", "resignation"]:
                del self.employees[action["details"]["employeePeopleSoftID"]]

    def visualize(self):

        edges = []

        # rankdir is BT (bottom top) to render with DG at the top
        mdccd = graphviz.Graph(
            name="Orthogonal",
            engine="dot",
            graph_attr={
                "rankdir": "BT",
                "label": "MDCCD Org Chart",
                "splines": "ortho",
            },
            node_attr={
                "shape": "none",
                "margin": "0",
                "fontname": "arial",
                "fontsize": "16",
            },
        )

        for position in self.positions:
            pp(self.positions[position])
            box = self.positions[position]
            incumbent_label = ""
            if box.get("incumbent", False):
                person = self.employees[box["incumbent"]]
                incumbent_label = f"{person["firstName"]} {person["lastName"]}"
            else:
                incumbent_label = "VACANT"
            label = f"""<
            <TABLE BORDER = "1" 
            BGCOLOR = "lightyellow" 
            CELLBORDER = "0" CELLPADDING = "1">
            <TR>
                <TD><B>{box["positionNumber"]}</B></TD>
            </TR>
            <TR>
                <TD>{incumbent_label}</TD>
            </TR>
            <TR>
                <TD>{box["title"]}</TD>
            </TR>
            <TR>
                <TD>{box["classification"]}</TD>
            </TR>
            <TR>
                <TD>{box["language"]}</TD>
            </TR>
            <TR>
                <TD>{box["security"]}</TD>
            </TR>
            <TR>
                <TD>{box["location"]}</TD>
            </TR>
            </TABLE>
            >"""
            mdccd.node(str(box["positionNumber"]), label=label)
            if box["reportsTo"]:
                edges.append((str(box["positionNumber"]), str(box["reportsTo"])))

        mdccd.edges(edges)

        mdccd.render("mdccd.gv", view=True)
