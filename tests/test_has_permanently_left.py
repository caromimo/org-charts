from automatedorgcharts import has_permanently_left


def test_has_permanently_left_with_employee_who_left():
    employee_who_left = {
        "directorate": "MDCCD",
        "division": "PPAD",
        "unit": "IMAP",
        "type": "Manager",
        "title": "Manager",
        "classificationAndLevel": "EC-07",
        "positionNumber": "32",
        "reportsTo": "29",
        "lastName": "Sanserre",
        "firstName": "Michelle",
        "employeeID": "13461",
        "tenure": "indeterminate",
        "staffingAction": "deploymentOUT",
        "startsOn": "2023-05-23",
        "endsOn": "",
    }
    assert has_permanently_left(employee_who_left) is True


def test_has_permanently_left_with_current_employee():
    current_employee = {
        "directorate": "MDCCD",
        "division": "PPAD",
        "unit": "IMAP",
        "type": "Manager",
        "title": "Manager",
        "classificationAndLevel": "EC-07",
        "positionNumber": "32",
        "reportsTo": "29",
        "lastName": "Muller",
        "firstName": "Cassandra",
        "employeeID": "53463",
        "tenure": "indeterminate",
        "staffingAction": "appointment",
        "startsOn": "2023-07-12",
        "endsOn": "",
    }
    assert has_permanently_left(current_employee) is False
