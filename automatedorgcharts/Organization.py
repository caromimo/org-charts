# resources: https://graphviz.readthedocs.io/en/stagoble/examples.html#hello-py
import graphviz
from automatedorgcharts import is_current_employee


class Organization:
    def __init__(self):
        self.employees = {}
        self.positions = {}

    def add_employee(self, row):
        self.employees[row["employeeID"]] = row

    def add_position(self, row):
        self.positions[row["positionNumber"]] = row
