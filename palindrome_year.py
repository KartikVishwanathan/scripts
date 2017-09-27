
'''Count the number of possible palindrome dates of the form MMDDYYYY in the century of the given year.
The dates can be either 7 digit or 8 digits. Note that date has to be of the form DD. ie '02' or '09'.
While month can be either of the form '2' or '02'. Check for palindrome in both the cases'''


def is_leap(year):
    if year % 4 == 0 and year % 400 != 0:
        return True
    else:
        return False

def is_palindrome(date):
    return date == date[::-1]


def palindrome_count(year):
    century = year - year % 100
    palindrome_count = 0
    if is_leap(year):
        days_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for month in range(0,12):
        for day in range(1, days_of_month[month] + 1):
            for year in range(century, century + 101):
                if 1 <= day <= 9:
                     day_str = '0' + str(day)
                else:
                     day_str = str(day)
                date_str = str(month+1) + day_str + str(year)
                if is_palindrome(date_str):
                    palindrome_count = palindrome_count + 1
                elif  not is_palindrome(date_str) and len(date_str)==7:
                    date_str = '0' + date_str
                    if is_palindrome(date_str):
                        palindrome_count = palindrome_count + 1
                
    return palindrome_count
