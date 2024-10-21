from datetime import datetime


def convert_to_date(date_string):
    """Change data type to date"""
    return datetime.strptime(date_string, "%Y-%m-%d").date()
