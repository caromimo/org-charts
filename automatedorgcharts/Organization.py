# import graphviz


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
            # if type is appointment... (TODO other instances of staffing)
            self.employees[action["details"]["peopleSoftID"]] = action["details"]
