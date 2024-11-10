from datetime import date
from .convert_to_date import convert_to_date


# RESOLVE TEMPORARY LEAVES
# identify assignmentOUT, secondmentOUT, interchange, maternity leave, paternity leave, parental leave, leave without pay (LWOP), sick LWOP (SLWOP)
def is_on_temporary_leave(row):
    if (
        row["staffingAction"] == "assignmentOUT"
        or row["staffingAction"] == "secondmentOUT"
        or row["staffingAction"] == "interchange"
        or row["staffingAction"] == "maternity leave"
        or row["staffingAction"] == "paternity leave"
        or row["staffingAction"] == "parental leave"
        or row["staffingAction"] == "LWOP"
        or row["staffingAction"] == "SLWOP"
    ):
        # if end date is in the future, employee is on temporary leave, return True
        end_date = convert_to_date(row["endsOn"])
        if end_date >= date.today():
            return True
        else:
            return False
    else:
        return False
