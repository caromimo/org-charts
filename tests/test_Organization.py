from automatedorgcharts import Organization
from automatedorgcharts import convert_to_date


def test_employee_on_parental_leave_is_not_included():
    position = {
        "action": "classification",
        "type": "create",
        "details": {
            "positionNumber": 7373,
            "title": "Policy Analyst",
            "classification": "EC-05",
            "language": "English",
            "security": "Reliability",
            "location": "Ottawa",
            "reportsTo": "1111",
            "effectiveDate": convert_to_date("2020-12-01"),
        },
    }

    appointment = {
        "action": "staffing",
        "type": "appointmentIN",
        "details": {
            "employeePeopleSoftID": 989898,
            "positionNumber": 7373,
            "firstName": "Ashley",
            "lastName": "Samson",
            "language": "English",
            "security": "Reliability",
            "tenure": "indeterminate",
            "startDate": convert_to_date("2022-01-01"),
        },
    }

    parental_leave = {
        "action": "staffing",
        "type": "parentalLeave",
        "details": {
            "employeePeopleSoftID": 989898,
            "startDate": convert_to_date("2024-01-01"),
            "endDate": convert_to_date("2025-09-01"),
        },
    }

    org = Organization()
    org.process_action(position)
    org.process_action(appointment)
    org.process_action(parental_leave)
    assert org.employees == {}
