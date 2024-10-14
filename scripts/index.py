import csv
from pprint import pp
from datetime import datetime, date

# start with an empty dictionary
output = {}


def is_current_employee(row):
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


def to_date(date_string):
    """Change data type to date"""
    return datetime.strptime(date_string, "%Y-%m-%d").date()


with open("./data/raw/data.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")
    for row in data:
        if is_current_employee(row):
            # have I seen this employee before?
            previous = output.get(row["employeeID"], None)
            if previous == None:
                # save information as never seen before
                output[row["employeeID"]] = row
            else:
                # seen this employee before, need to decide which staffing action to keep
                # select the most recent staffing action start date for employee
                # get the start date of the current row
                current_row_start_date = to_date(row["startsOn"])
                # compare to start date of existing record for employee
                # keep if start date for current is larger/later than previous
                if current_row_start_date > to_date(previous["startsOn"]):
                    output[row["employeeID"]] = row

pp(output)
