# import graphviz
from datetime import date


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

            if action["type"] in ["appointment", "deploymentIN"]:
                self.employees[action["details"]["employeePeopleSoftID"]] = action[
                    "details"
                ]

            if action["type"] == "parentalLeave":
                if action["details"]["endDate"] > date.today():
                    del self.employees[action["details"]["employeePeopleSoftID"]]

            if action["type"] in ["deploymentOUT", "retirement", "resignation"]:
                del self.employees[action["details"]["employeePeopleSoftID"]]
