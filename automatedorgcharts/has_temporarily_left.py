from datetime import date
from .to_date import to_date


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
