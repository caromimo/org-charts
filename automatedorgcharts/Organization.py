# resources: https://graphviz.readthedocs.io/en/stagoble/examples.html#hello-py
import graphviz
from automatedorgcharts import is_current_employee


class Organization:
    def __init__(self):
        self.employees = {}

    def add_employee(self, row):
        if is_current_employee(row):
            self.employees[row["employeeID"]] = row
