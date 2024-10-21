import csv
from pprint import pp
from automatedorgcharts import convert_to_date, is_current_employee

# start with an empty dictionary
output = {}


with open("./data/raw/data.csv") as csvfile:
    data = csv.DictReader(csvfile, delimiter=",")
    for row in data:
        if is_current_employee(row):
            # have I seen this employee before?
            previous = output.get(row["employeeID"], None)
            if previous is None:
                # save information as never seen before
                output[row["employeeID"]] = row
            else:
                # seen this employee before, need to decide which staffing action to keep
                # select the most recent staffing action start date for employee
                # get the start date of the current row
                current_row_start_date = convert_to_date(row["startsOn"])
                # compare to start date of existing record for employee
                # keep if start date for current is larger/later than previous
                if current_row_start_date > convert_to_date(previous["startsOn"]):
                    output[row["employeeID"]] = row

pp(output)
