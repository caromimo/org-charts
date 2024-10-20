from automatedorgcharts import has_permanently_left


def test_has_permanently_left_with_employee_who_left():
    employee_who_left = {
        "directorate": "MDCCD",
        "division": "PPAD",
        "unit": "IMAP",
        "positionType": "Manager",
        "positionTitle": "Manager",
        "positionClassificationAndLevel": "EC-07",
        "positionNumber": "32",
        "positionReportsTo": "29",
        "employeeeLastName": "Sanserre",
        "employeeFirstName": "Michelle",
        "employeeID": "13461",
        "employeeTenure": "indeterminate",
        "staffingActionType": "deploymentOUT",
        "startsOn": "2023-05-23",
        "endsOn": "",
    }
    assert has_permanently_left(employee_who_left) is True


def test_has_permanently_left_with_current_employee():
    current_employee = {
        "directorate": "MDCCD",
        "division": "PPAD",
        "unit": "IMAP",
        "positionType": "Manager",
        "positionTitle": "Manager",
        "positionClassificationAndLevel": "EC-07",
        "positionNumber": "32",
        "positionReportsTo": "29",
        "employeeeLastName": "Muller",
        "employeeFirstName": "Cassandra",
        "employeeID": "53463",
        "employeeTenure": "indeterminate",
        "staffingActionType": "appointment",
        "startsOn": "2023-07-12",
        "endsOn": "",
    }
    assert has_permanently_left(current_employee) is False
