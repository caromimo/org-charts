from automatedorgcharts import is_current_employee


def test_is_current_employee_with_current_employee():
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
    assert is_current_employee(current_employee) is True


# be careful as this will eventually fail depending on date run
def test_is_current_employee_with_acting_employee():
    acting_employee = {
        "directorate": "MDCCD",
        "division": "PPAD",
        "unit": "IMAP",
        "type": "Employee",
        "title": "Admin Assit",
        "classificationAndLevel": "AS-04",
        "positionNumber": "87",
        "reportsTo": "32",
        "lastName": "Fortin",
        "firstName": "Jean",
        "employeeID": "99876",
        "tenure": "indeterminate",
        "staffingAction": "acting",
        "startsOn": "2023-07-04",
        "endsOn": "2024-11-03",
    }
    assert (
        is_current_employee(acting_employee) is True
    ), "Should be true if test is run on a date before the endsOn date of the acting."


def test_is_current_employee_with_deployedOUT_employee():
    deployed_employee = {
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
    assert is_current_employee(deployed_employee) is False


def test_is_current_employee_with_secondmentOUT_employee():
    secondmentOUT_employee = {
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
    assert is_current_employee(secondmentOUT_employee) is False
