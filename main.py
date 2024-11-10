import csv
from pprint import pp
from automatedorgcharts import Organization

mdccd = Organization()

with open("./data/processed/people.csv") as csvfile:
    people = csv.DictReader(csvfile, delimiter=",")
    for row in people:
        mdccd.add_employee(row)

pp(mdccd.employees)
