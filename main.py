import csv
from pprint import pp
from automatedorgcharts import Organization

mdccd = Organization()

with open("./data/processed/people.csv") as csvfile:
    people = csv.DictReader(csvfile, delimiter=",")
    for row in people:
        mdccd.add_employee(row)

with open("./data/processed/positions.csv") as csvfile:
    positions = csv.DictReader(csvfile, delimiter=",")
    for row in positions:
        mdccd.add_position(row)

pp(mdccd.employees)
pp(mdccd.positions)
