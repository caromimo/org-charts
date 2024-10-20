from .has_permanently_left import has_permanently_left
from .has_temporarily_left import has_temporarily_left


# IDENTIFY CURRENT EMPLOYEES
# identify who has not left permanently or temporarly
def is_current_employee(row):
    if has_permanently_left(row):
        return False
    if has_temporarily_left(row):
        return False
    else:
        return True
