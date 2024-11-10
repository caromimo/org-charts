# RESOLVE PERMANENT LEAVES
# identify deploymentOUT, retirement, and resignation


def has_permanently_left(row):
    if (
        row["staffingAction"] == "deploymentOUT"
        or row["staffingAction"] == "retirement"
        or row["staffingAction"] == "resignation"
    ):
        return True
    else:
        return False
