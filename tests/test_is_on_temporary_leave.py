from automatedorgcharts import is_on_temporary_leave


def test_is_on_temporary_leave_with_employee_on_secondmentOUT():
    employee_on_secondmentOUT = {
        "directorate": "MDCCD",
        "division": "MDCP",
        "unit": "NA",
        "type": "Director",
        "title": "Director",
        "classificationAndLevel": "EX-01",
        "positionNumber": "30",
        "reportsTo": "28",
        "lastName": "Moon",
        "firstName": "Chadley",
        "employeeID": "22315",
        "tenure": "indeterminate",
        "staffingAction": "secondmentOUT",
        "startsOn": "2023-03-01",
        "endsOn": "2025-05-02",
    }
    assert is_on_temporary_leave(employee_on_secondmentOUT) is True


def test_is_on_temporary_leave_with_employee_on_secondmentOUT_who_returned():
    employee_on_secondmentOUT_who_returned = {
        "directorate": "MDCCD",
        "division": "MDCP",
        "unit": "NA",
        "type": "Director",
        "title": "Director",
        "classificationAndLevel": "EX-01",
        "positionNumber": "30",
        "reportsTo": "28",
        "lastName": "Courmayeur",
        "firstName": "Brad",
        "employeeID": "28815",
        "tenure": "indeterminate",
        "staffingAction": "secondmentOUT",
        "startsOn": "2021-11-01",
        "endsOn": "2022-05-12",
    }
    assert is_on_temporary_leave(employee_on_secondmentOUT_who_returned) is False


def test_is_on_temporary_leave_with_current_employee():
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
    assert is_on_temporary_leave(current_employee) is False
