# IDENTIFY DETERMINATE STAFFING ACTIONS
# identify term, contract, student hiring offer, assignmentIN, secondmentIN, and acting


def is_in_determinate_position(row):
    if (
        row["staffingActionType"] == "term"
        or row["staffingActionType"] == "contract"
        or row["staffingActionType"] == "student hiring offer"
        or row["staffingActionType"] == "assignmentIN"
        or row["staffingActionType"] == "secondmentIN"
        or row["staffingActionType"] == "acting"
    ):
        return True
    else:
        return False
