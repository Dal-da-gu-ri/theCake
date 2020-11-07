from home.models import *
from datetime import datetime

def mappingDate(businessID,month, date):
    available = False
    curmonth = datetime.today().month
    storeAmount = DailyAmount.objects.get(businessID=businessID)
    print(curmonth,month,date)

    if curmonth == month:
        if date == 1:
            if storeAmount.day1 > 0:
                available = True
        elif date == 2:
            if storeAmount.day2 > 0:
                available = True
        elif date == 3:
            if storeAmount.day3 > 0:
                available = True
        elif date == 4:
            if storeAmount.day4 > 0:
                available = True
        elif date == 5:
            if storeAmount.day5 > 0:
                available = True
        elif date == 6:
            if storeAmount.day6 > 0:
                available = True
        elif date == 7:
            if storeAmount.day7 > 0:
                available = True
        elif date == 8:
            if storeAmount.day8 > 0:
                available = True
        elif date == 9:
            if storeAmount.day9 > 0:
                available = True
        elif date == 10:
            if storeAmount.day10 > 0:
                available = True
        elif date == 11:
            if storeAmount.day11 > 0:
                available = True
        elif date == 12:
            if storeAmount.day12 > 0:
                available = True
        elif date == 13:
            if storeAmount.day13 > 0:
                available = True
        elif date == 14:
            if storeAmount.day14 > 0:
                available = True
        elif date == 15:
            if storeAmount.day16 > 0:
                available = True
        elif date == 16:
            if storeAmount.day16 > 0:
                available = True
        elif date == 17:
            if storeAmount.day17 > 0:
                available = True
        elif date == 18:
            if storeAmount.day18 > 0:
                available = True
        elif date == 19:
            if storeAmount.day19 > 0:
                available = True
        elif date == 20:
            if storeAmount.day20 > 0:
                available = True
        elif date == 21:
            if storeAmount.day21 > 0:
                available = True
        elif date == 22:
            if storeAmount.day22 > 0:
                available = True
        elif date == 23:
            if storeAmount.day23 > 0:
                available = True
        elif date == 24:
            if storeAmount.day24 > 0:
                available = True
        elif date == 25:
            if storeAmount.day25 > 0:
                available = True
        elif date == 26:
            if storeAmount.day26 > 0:
                available = True
        elif date == 27:
            if storeAmount.day27 > 0:
                available = True
        elif date == 28:
            if storeAmount.day28 > 0:
                available = True
        elif date == 29:
            if storeAmount.day29 > 0:
                available = True
        elif date == 30:
            if storeAmount.day30 > 0:
                available = True
        elif date == 31:
            if storeAmount.day31 > 0:
                available = True
    elif curmonth != month:
        if date == 1:
            if storeAmount.day32 > 0:
                available = True
        elif date == 2:
            if storeAmount.day33 > 0:
                available = True
        elif date == 3:
            if storeAmount.day34 > 0:
                available = True
        elif date == 4:
            if storeAmount.day35 > 0:
                available = True
        elif date == 5:
            if storeAmount.day36 > 0:
                available = True
        elif date == 6:
            if storeAmount.day37 > 0:
                available = True
        elif date == 7:
            if storeAmount.day38 > 0:
                available = True
        elif date == 8:
            if storeAmount.day39 > 0:
                available = True
        elif date == 9:
            if storeAmount.day40 > 0:
                available = True
        elif date == 10:
            if storeAmount.day41 > 0:
                available = True
        elif date == 11:
            if storeAmount.day42 > 0:
                available = True
        elif date == 12:
            if storeAmount.day43 > 0:
                available = True
        elif date == 13:
            if storeAmount.day44 > 0:
                available = True
        elif date == 14:
            if storeAmount.day45 > 0:
                available = True
        elif date == 15:
            if storeAmount.day46 > 0:
                available = True
        elif date == 16:
            if storeAmount.day47 > 0:
                available = True
        elif date == 17:
            if storeAmount.day48 > 0:
                available = True
        elif date == 18:
            if storeAmount.day49 > 0:
                available = True
        elif date == 19:
            if storeAmount.day50 > 0:
                available = True
        elif date == 20:
            if storeAmount.day51 > 0:
                available = True
        elif date == 21:
            if storeAmount.day52 > 0:
                available = True
        elif date == 22:
            if storeAmount.day53 > 0:
                available = True
        elif date == 23:
            if storeAmount.day54 > 0:
                available = True
        elif date == 24:
            if storeAmount.day55 > 0:
                available = True
        elif date == 25:
            if storeAmount.day56 > 0:
                available = True
        elif date == 26:
            if storeAmount.day57 > 0:
                available = True
        elif date == 27:
            if storeAmount.day58 > 0:
                available = True
        elif date == 28:
            if storeAmount.day59 > 0:
                available = True
        elif date == 29:
            if storeAmount.day60 > 0:
                available = True
        elif date == 30:
            if storeAmount.day61 > 0:
                available = True
        elif date == 31:
            if storeAmount.day62 > 0:
                available = True
    print(available)
    return available
