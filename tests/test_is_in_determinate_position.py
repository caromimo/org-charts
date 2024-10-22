from automatedorgcharts import is_in_determinate_position


def test_is_in_determinate_position_with_employee_on_assignment():
    employee_on_assignment = {
        "directorate": "MDCCD",
        "division": "MDCP",
        "unit": "IMAP",
        "positionType": "Employee",
        "positionTitle": "Analyst",
        "positionClassificationAndLevel": "EC-05",
        "positionNumber": "25",
        "positionReportsTo": "32",
        "employeeeLastName": "Stonehead",
        "employeeFirstName": "Nadira",
        "employeeID": "11353",
        "employeeTenure": "indeterminate",
        "staffingActionType": "assignmentIN",
        "startsOn": "2023-03-04",
        "endsOn": "2024-02-27",
    }
    assert is_in_determinate_position(employee_on_assignment) is True
