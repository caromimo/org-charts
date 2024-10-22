from automatedorgcharts import is_in_indeterminate_position


def test_is_in_indeterminate_position_with_indeterminate_employee():
    indeterminate_employee = {
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
    assert is_in_indeterminate_position(indeterminate_employee) is True
