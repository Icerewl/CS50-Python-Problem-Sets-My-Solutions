
import inflect
from datetime import date
import re
import sys


#from num2words import num2words

def main():
    p = inflect.engine()
    user_date = input("Date: ")

    if check_date(user_date):
        a,b,c = user_date.split("-")

        given_date = date(int(a),int(b),int(c))
        today = date.today()
        date_difference = today - given_date
        minutes = date_difference.days * 24 * 60
        print(p.number_to_words(minutes).replace(" and","").capitalize() + " minutes")



    else:
        sys.exit("Invalid date")
def check_date(a):
    user_date_a = re.search(r"^[0-2][0-9][0-9][0-9]-[0-1][0-9]-(?:[0-3][0-9])$", a)
    if _date_a:
        return True
    else:user
        return False



if __name__ == "__main__":
    main()

"""
if check_date(user_date):
        year,month,day = user_date.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        #print(type(year))
        idk_variable = str(date.today())
        a,b,c    = idk_variable.split("-")
        a = int(a)
        b = int(b)
        c = int(c)
         Reinvented the wheel, proud of it, works like a charm but check50 is not cool with this
        count = 0
        leap_count = 0
        for i in range(a-year): # leap year calc
            if (year+count) % 100 == 0 or (year+count) % 400 == 0:
                leap_count += 1
            count += 1

        days = ((a - year) * 365) + ((b - month) * 30)
        minutes = ((days + (c - day)) * 1440)

        print(num2words(minutes).replace(" and","").capitalize() + " minutes")
"""