from datetime import date
from .to_date import to_date

# from automatedorgcharts import to_date


# RESOLVE PERMANENT LEAVES
# identify deploymentOUT, retirement, and resignation
def has_permanently_left(row):
    if (
        row["staffingActionType"] == "deploymentOUT"
        or row["staffingActionType"] == "retirement"
        or row["staffingActionType"] == "resignation"
    ):
        return True
    else:
        return False


# RESOLVE TEMPORARY LEAVES
# identify assignmentOUT, secondmentOUT, maternity leave, paternity leave, parental leave, leave without pay (LWOP), sick LWOP (SLWOP)
def has_temporarily_left(row):
    if (
        row["staffingActionType"] == "assignmentOUT"
        or row["staffingActionType"] == "secondmentOUT"
        or row["staffingActionType"] == "maternity leave"
        or row["staffingActionType"] == "paternity leave"
        or row["staffingActionType"] == "parental leave"
        or row["staffingActionType"] == "LWOP"
        or row["staffingActionType"] == "SLWOP"
    ):
        # if end date is in the future, employee is on temporary leave, return True
        end_date = to_date(row["endsOn"])
        if end_date >= date.today():
            return True
        else:
            return False
    else:
        return False


# IDENTIFY CURRENT EMPLOYEES
# identify who has not left permanently or temporarly
def is_current_employee(row):
    if has_permanently_left(row):
        return False
    if has_temporarily_left(row):
        return False
    else:
        return True
