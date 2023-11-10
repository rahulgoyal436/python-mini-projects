# calculate.py
def judge_leap_year(year):
    if year is None or not isinstance(year, int):
        raise TypeError('year must be integer if not None')
    if year < 1:
        raise ValueError('Year must be a positive integer')
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
