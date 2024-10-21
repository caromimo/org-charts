from .has_permanently_left import has_permanently_left
from .is_on_temporary_leave import is_on_temporary_leave


# IDENTIFY CURRENT EMPLOYEES
# identify who has not left permanently or temporarly
def is_current_employee(row):
    if has_permanently_left(row):
        return False
    if is_on_temporary_leave(row):
        return False
    else:
        return True
