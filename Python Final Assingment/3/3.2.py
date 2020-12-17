import datetime
def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if month==12:
        return 31
    else:
        date1 = datetime.date(year, month, 1)
        date2 = datetime.date(year, month+1, 1)
        difference = date2 - date1
        return(difference.days) 
#print(days_in_month(2012,2))
