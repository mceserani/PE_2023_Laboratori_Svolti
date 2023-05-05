def is_year_leap(year):
    """
    Determine if a given year is a leap year or not.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def days_in_month(year, month):
    """
    Determine the number of days in a given month of a given year.

    Args:
        year (int): The year to check.
        month (int): The month to check.

    Returns:
        int: The number of days in the given month of the given year.
    """
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31
