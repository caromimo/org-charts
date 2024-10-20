from automatedorgcharts import has_temporarily_left


def test_has_temporarily_left_with_employee_on_secondmentOUT():
    employee_on_secondmentOUT = {
        "directorate": "MDCCD",
        "division": "MDCP",
        "unit": "NA",
        "positionType": "Director",
        "positionTitle": "Director",
        "positionClassificationAndLevel": "EX-01",
        "positionNumber": "30",
        "positionReportsTo": "28",
        "employeeeLastName": "Moon",
        "employeeFirstName": "Chadley",
        "employeeID": "22315",
        "employeeTenure": "indeterminate",
        "staffingActionType": "secondmentOUT",
        "startsOn": "2023-03-01",
        "endsOn": "2025-05-02",
    }
    assert has_temporarily_left(employee_on_secondmentOUT) is True


def test_has_temporarily_left_with_employee_on_secondmentOUT_who_returned():
    employee_on_secondmentOUT_who_returned = {
        "directorate": "MDCCD",
        "division": "MDCP",
        "unit": "NA",
        "positionType": "Director",
        "positionTitle": "Director",
        "positionClassificationAndLevel": "EX-01",
        "positionNumber": "30",
        "positionReportsTo": "28",
        "employeeeLastName": "Courmayeur",
        "employeeFirstName": "Brad",
        "employeeID": "28815",
        "employeeTenure": "indeterminate",
        "staffingActionType": "secondmentOUT",
        "startsOn": "2021-11-01",
        "endsOn": "2022-05-12",
    }
    assert has_temporarily_left(employee_on_secondmentOUT_who_returned) is False


def test_has_temporarily_left_with_current_employee():
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
    assert has_temporarily_left(current_employee) is False
