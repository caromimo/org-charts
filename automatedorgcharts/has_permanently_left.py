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
