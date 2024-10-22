# DETERMINE IF INDETERMINATE POSITION
# identify appointment, deploymentIN, transferIN


def is_in_indeterminate_position(row):
    if (
        row["staffingActionType"] == "appointment"
        or row["staffingActionType"] == "deploymentIN"
        or row["staffingActionType"] == "transferIN"
    ):
        return True
    else:
        return False
