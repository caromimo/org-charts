from datetime import datetime, date

# from automatedorgcharts import to_date


def is_current_employee(row):
    """Identifies all current employees."""
    # if employee deployedOUT, return False
    if (
        row["staffingActionType"] == "deploymentOUT"
        or row["staffingActionType"] == "secondmentOUT"
    ):
        return False
    # if no end date, current employee, return True
    if row["endsOn"] == "":
        return True
    # if end date in the future, current employee, return True
    end_date = datetime.strptime(row["endsOn"], "%Y-%m-%d").date()
    if end_date > date.today():
        return True
    else:
        return False
