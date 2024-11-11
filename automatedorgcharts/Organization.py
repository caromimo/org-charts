# import graphviz


class Organization:
    def __init__(self):
        self.employees = {}
        self.positions = {}

    def process_action(self, action):
        if action["action"] == "classification":
            # if type is create... (TODO other instances of classification)
            self.positions[action["details"]["positionNumber"]] = action["details"]
        if action["action"] == "staffing":
            # if type is appointment... (TODO other instances of staffing)
            self.employees[action["details"]["peopleSoftID"]] = action["details"]
