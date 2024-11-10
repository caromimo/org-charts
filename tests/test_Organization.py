from automatedorgcharts import Organization

employee1 = {
    "directorate": "MDCCD",
    "division": "PPAD",
    "unit": "IMAP",
    "positionType": "Manager",
    "positionTitle": "Manager",
    "positionClassificationAndLevel": "EC-07",
    "positionNumber": "32",
    "reportsToPositionNumber": "29",
    "lastName": "Muller",
    "firstName": "Cassandra",
    "employeeID": "53463",
    "employeeTenure": "indeterminate",
    "staffingActionType": "appointment",
    "startsOn": "2023-07-12",
    "endsOn": "",
}

employee2 = {
    "directorate": "MDCCD",
    "division": "PPAD",
    "unit": "IMAP",
    "positionType": "Employee",
    "positionTitle": "Admin Assit",
    "positionClassificationAndLevel": "AS-04",
    "positionNumber": "87",
    "reportsToPositionNumber": "32",
    "lastName": "Fortin",
    "firstName": "Jean",
    "employeeID": "99876",
    "employeeTenure": "indeterminate",
    "staffingActionType": "acting",
    "startsOn": "2023-07-04",
    "endsOn": "2024-11-03",
}

employee3 = {
    "directorate": "MDCCD",
    "division": "MDCP",
    "unit": "IMAP",
    "positionType": "Employee",
    "positionTitle": "Analyst",
    "positionClassificationAndLevel": "EC-05",
    "positionNumber": "25",
    "reportsToPositionNumber": "32",
    "lastName": "Stonehead",
    "firstName": "Nadira",
    "employeeID": "11353",
    "employeeTenure": "indeterminate",
    "staffingActionType": "assignmentIN",
    "startsOn": "2023-03-04",
    "endsOn": "2024-02-27",
}

employee4 = {
    "directorate": "MDCCD",
    "division": "",
    "unit": "",
    "positionType": "DG",
    "positionTitle": "Executive",
    "positionClassificationAndLevel": "EX-02",
    "positionNumber": "29",
    "reportsToPositionNumber": "",
    "lastName": "Langelin",
    "firstName": "Cindy",
    "employeeID": "12343",
    "employeeTenure": "indeterminate",
    "staffingActionType": "appointment",
    "startsOn": "2023-02-12",
    "endsOn": "",
}


def test_good_Organization():
    org = Organization()
    org.add_staffing_action(employee1)
    org.add_staffing_action(employee2)
    org.add_staffing_action(employee3)
    org.add_staffing_action(employee4)
    org.graph.view()
    assert org.graph.source == "popcorn"
