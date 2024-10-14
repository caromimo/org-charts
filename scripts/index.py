import csv
from pprint import pp
from datetime import datetime, date

# start with an empty dictionary
output = {}


def is_current_employee(data):
    """Identifies all current employees."""
    # if no end date, current employee, return True
    if row["endsOn"] == "":
        return True
    # if end date in the future, current employee, return True
    end_date = datetime.strptime(row["endsOn"], "%Y-%m-%d").date()
    if end_date > date.today():
        return True
    else:
        return False


with open("./data/raw/data.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")
    for row in data:
        if is_current_employee(row):
            output[row["employeeID"]] = row


pp(output)
