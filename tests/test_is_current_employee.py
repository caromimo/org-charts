from automatedorgcharts import is_current_employee


def test_is_current_employee_with_current_employee():
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
    assert is_current_employee(current_employee) is True


# be careful as this will eventually fail depending on date run
def test_is_current_employee_with_acting_employee():
    acting_employee = {
        "directorate": "MDCCD",
        "division": "PPAD",
        "unit": "IMAP",
        "positionType": "Employee",
        "positionTitle": "Admin Assit",
        "positionClassificationAndLevel": "AS-04",
        "positionNumber": "87",
        "positionReportsTo": "32",
        "employeeeLastName": "Fortin",
        "employeeFirstName": "Jean",
        "employeeID": "99876",
        "employeeTenure": "indeterminate",
        "staffingActionType": "acting",
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
    assert is_current_employee(deployed_employee) is False


def test_is_current_employee_with_secondmentOUT_employee():
    secondmentOUT_employee = {
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
    assert is_current_employee(secondmentOUT_employee) is False
