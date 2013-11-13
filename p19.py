weekday = 0
month = 0
year = 1900
day = 1
days = {0:31,1:28,2:31,3:30,4:31,5:30,6:31,7:31,8:30,9:31,10:30,11:31}
leap_days = {0:31,1:29,2:31,3:30,4:31,5:30,6:31,7:31,8:30,9:31,10:30,11:31}

def is_leap(yr):
    if yr % 4 == 0:
        if yr % 100 == 0:
            if yr % 400 == 0:
                return True
            else:
                return False
        
        return True
    else:
        return False
        
count = 0

while year < 2001:
    weekday = weekday % 7
    month = month % 12
    
    if day > days[month]:
        day = 1
        month += 1
        if month == 12:
            month = 0
            year += 1
        
        if weekday == 6 and year > 1900:
            count += 1
    else:
        day += 1
        weekday += 1
        
print count