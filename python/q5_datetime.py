# Hint:  use Google to find python function

from datetime import date
#function to subtract time and return answer in readable form
def calc_days(start, stop):
    return("There are " + str((stop - start).days) + " days between these dates.")
####a)
date_start = '01-02-2013'  
date_stop = '07-28-2015' 
#reassign date in code readable form
date_start = date(2013, 1, 2)
date_stop = date(2015, 7, 28)
print(calc_days(date_start, date_stop))
####b)  
date_start = '12312013'  
date_stop = '05282015'
#reassign date in code readable form
date_start = date(2013,12,31)
date_stop = date(2015,5,28)
print(calc_days(date_start, date_stop))
####c)
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'
#reassign date in code readable form
date_start = date(1994, 1, 15)
date_stop = date(2015, 7, 14)
print(calc_days(date_start, date_stop))
 
