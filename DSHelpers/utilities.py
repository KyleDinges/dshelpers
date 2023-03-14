import calendar

def get_last_day_of_month(year, month):
    '''
      Returns the final day of the month based on the year and month of a date.
      For example get_last_day_of_month(2023, 02) would return 28.

      Parameters
      ----------
      year: int
        Year
      month: int
        Month
      Returns
      day: int
        The last day of the month as an integer
      -------

      Examples
      --------
      final_day = get_last_day_of_month(2023, 02)
      print(final_day)

      '''
    # get the final day of the month for each month and year combination
    day = calendar.monthrange(year, month)[1]
    return day

