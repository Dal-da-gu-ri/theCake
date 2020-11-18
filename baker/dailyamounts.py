from datetime import datetime
from home.models import *

def setDailyAmounts(businessID,sunday,monday,tuesday,wednesday,thursday,friday,saturday):

    date = datetime.today().day
    yoil = datetime.weekday(datetime.today())
    try:
        dailyobject = DailyAmount.objects.get(businessID=businessID)

        if yoil == 0:  # 월요일
            if date % 7 == 0:
                set1, set2, set3, set4, set5, set6, set7 = tuesday,wednesday,thursday,friday,saturday,sunday, monday

            elif date % 7 == 1:
                set1, set2, set3, set4, set5, set6, set7 = monday,tuesday,wednesday,thursday,friday,saturday,sunday

            elif date % 7 == 2:
                set1, set2, set3, set4, set5, set6, set7 = sunday, monday,tuesday,wednesday,thursday,friday,saturday

            elif date % 7 == 3:
                set1, set2, set3, set4, set5, set6, set7 = saturday,sunday, monday,tuesday,wednesday,thursday,friday

            elif date % 7 == 4:
                set1, set2, set3, set4, set5, set6, set7 = friday,saturday,sunday, monday,tuesday,wednesday,thursday

            elif date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = thursday,friday,saturday,sunday, monday,tuesday,wednesday

            elif date % 7 == 6:
                set1, set2, set3, set4, set5, set6, set7 = wednesday,thursday,friday,saturday,sunday, monday,tuesday

        elif yoil == 1:  # 화요일
            if date % 7 == 1:
                set1, set2, set3, set4, set5, set6, set7 = tuesday,wednesday,thursday,friday,saturday,sunday, monday

            elif date % 7 == 2:
                set1, set2, set3, set4, set5, set6, set7 = monday,tuesday,wednesday,thursday,friday,saturday,sunday

            elif date % 7 == 3:
                set1, set2, set3, set4, set5, set6, set7 = sunday, monday,tuesday,wednesday,thursday,friday,saturday

            elif date % 7 == 4:
                set1, set2, set3, set4, set5, set6, set7 = saturday,sunday, monday,tuesday,wednesday,thursday,friday

            elif date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = friday,saturday,sunday, monday,tuesday,wednesday,thursday

            elif date % 7 == 6:
                set1, set2, set3, set4, set5, set6, set7 = thursday,friday,saturday,sunday, monday,tuesday,wednesday

            elif date % 7 == 0:
                set1, set2, set3, set4, set5, set6, set7 = wednesday,thursday,friday,saturday,sunday, monday,tuesday

        elif yoil == 2:  # 수요일
            if date % 7 == 2:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

            elif date % 7 == 3:
                set1, set2, set3, set4, set5, set6, set7 = monday, tuesday, wednesday, thursday, friday, saturday, sunday

            elif date % 7 == 4:
                set1, set2, set3, set4, set5, set6, set7 = sunday, monday, tuesday, wednesday, thursday, friday, saturday

            elif date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = saturday, sunday, monday, tuesday, wednesday, thursday, friday

            elif date % 7 == 6:
                set1, set2, set3, set4, set5, set6, set7 = friday, saturday, sunday, monday, tuesday, wednesday, thursday

            elif date % 7 == 0:
                set1, set2, set3, set4, set5, set6, set7 = thursday, friday, saturday, sunday, monday, tuesday, wednesday

            elif date % 7 == 1:
                set1, set2, set3, set4, set5, set6, set7 = wednesday, thursday, friday, saturday, sunday, monday, tuesday

        elif yoil == 3:  # 목요일
            if date % 7 == 3:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

            elif date % 7 == 4:
                set1, set2, set3, set4, set5, set6, set7 = monday, tuesday, wednesday, thursday, friday, saturday, sunday

            elif date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = sunday, monday, tuesday, wednesday, thursday, friday, saturday

            elif date % 7 == 6:
                set1, set2, set3, set4, set5, set6, set7 = saturday, sunday, monday, tuesday, wednesday, thursday, friday

            elif date % 7 == 0:
                set1, set2, set3, set4, set5, set6, set7 = friday, saturday, sunday, monday, tuesday, wednesday, thursday

            elif date % 7 == 1:
                set1, set2, set3, set4, set5, set6, set7 = thursday, friday, saturday, sunday, monday, tuesday, wednesday

            elif date % 7 == 2:
                set1, set2, set3, set4, set5, set6, set7 = wednesday, thursday, friday, saturday, sunday, monday, tuesday

        elif yoil == 4:  # 금요일
            if date % 7 == 4:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

            elif date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = sunday, monday, tuesday, wednesday, thursday, friday, saturday

            elif date % 7 == 6:
                set1, set2, set3, set4, set5, set6, set7 = sunday, monday, tuesday, wednesday, thursday, friday, saturday

            elif date % 7 == 0:
                set1, set2, set3, set4, set5, set6, set7 = saturday, sunday, monday, tuesday, wednesday, thursday, friday

            elif date % 7 == 1:
                set1, set2, set3, set4, set5, set6, set7 = friday, saturday, sunday, monday, tuesday, wednesday, thursday

            elif date % 7 == 2:
                set1, set2, set3, set4, set5, set6, set7 = thursday, friday, saturday, sunday, monday, tuesday, wednesday

            elif date % 7 == 3:
                set1, set2, set3, set4, set5, set6, set7 = wednesday, thursday, friday, saturday, sunday, monday, tuesday

        elif yoil == 5:  # 토요일
            if date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

            elif date % 7 == 6:
                set1, set2, set3, set4, set5, set6, set7 = monday, tuesday, wednesday, thursday, friday, saturday, sunday

            elif date % 7 == 0:
                set1, set2, set3, set4, set5, set6, set7 = sunday, monday, tuesday, wednesday, thursday, friday, saturday

            elif date % 7 == 1:
                set1, set2, set3, set4, set5, set6, set7 = saturday, sunday, monday, tuesday, wednesday, thursday, friday

            elif date % 7 == 2:
                set1, set2, set3, set4, set5, set6, set7 = friday, saturday, sunday, monday, tuesday, wednesday, thursday

            elif date % 7 == 3:
                set1, set2, set3, set4, set5, set6, set7 = thursday, friday, saturday, sunday, monday, tuesday, wednesday

            elif date % 7 == 4:
                set1, set2, set3, set4, set5, set6, set7 = wednesday, thursday, friday, saturday, sunday, monday, tuesday

        elif yoil == 6:  # 일요일
            if date % 7 == 6:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

            elif date % 7 == 0:
                set1, set2, set3, set4, set5, set6, set7 = monday, tuesday, wednesday, thursday, friday, saturday, sunday

            elif date % 7 == 1:
                set1, set2, set3, set4, set5, set6, set7 = sunday, monday, tuesday, wednesday, thursday, friday, saturday

            elif date % 7 == 2:
                set1, set2, set3, set4, set5, set6, set7 = saturday, sunday, monday, tuesday, wednesday, thursday, friday

            elif date % 7 == 3:
                set1, set2, set3, set4, set5, set6, set7 = friday, saturday, sunday, monday, tuesday, wednesday, thursday

            elif date % 7 == 4:
                set1, set2, set3, set4, set5, set6, set7 = thursday, friday, saturday, sunday, monday, tuesday, wednesday

            elif date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = wednesday, thursday, friday, saturday, sunday, monday, tuesday

        dailyobject.day1 = set1
        dailyobject.day8 = set1
        dailyobject.day15 = set1
        dailyobject.day22 = set1
        dailyobject.day29 = set1
        dailyobject.day36 = set1
        dailyobject.day43 = set1
        dailyobject.day50 = set1
        dailyobject.day57 = set1
        # dailyobject.day32 = set1
        # dailyobject.day39 = set1
        # dailyobject.day46 = set1
        # dailyobject.day53 = set1
        # dailyobject.day60 = set1

        dailyobject.day2 = set2
        dailyobject.day9 = set2
        dailyobject.day16 = set2
        dailyobject.day23 = set2
        dailyobject.day30 = set2
        dailyobject.day37 = set2
        dailyobject.day44 = set2
        dailyobject.day51 = set2
        dailyobject.day58 = set2
        # dailyobject.day33 = set2
        # dailyobject.day40 = set2
        # dailyobject.day47 = set2
        # dailyobject.day54 = set2
        # dailyobject.day61 = set2

        dailyobject.day3 = set3
        dailyobject.day10 = set3
        dailyobject.day17 = set3
        dailyobject.day24 = set3
        dailyobject.day31 = set3
        dailyobject.day38 = set3
        dailyobject.day45 = set3
        dailyobject.day52 = set3
        dailyobject.day59 = set3
        # dailyobject.day34 = set3
        # dailyobject.day41 = set3
        # dailyobject.day48 = set3
        # dailyobject.day55 = set3
        # dailyobject.day62 = set3

        dailyobject.day4 = set4
        dailyobject.day11 = set4
        dailyobject.day18 = set4
        dailyobject.day25 = set4
        dailyobject.day32 = set4
        dailyobject.day39 = set4
        dailyobject.day46 = set4
        dailyobject.day53 = set4
        dailyobject.day60 = set4

        # dailyobject.day35 = set4
        # dailyobject.day42 = set4
        # dailyobject.day49 = set4
        # dailyobject.day56 = set4

        dailyobject.day5 = set5
        dailyobject.day12 = set5
        dailyobject.day19 = set5
        dailyobject.day26 = set5
        dailyobject.day33 = set5
        dailyobject.day40 = set5
        dailyobject.day47 = set5
        dailyobject.day54 = set5
        dailyobject.day61 = set5

        # dailyobject.day36 = set5
        # dailyobject.day43 = set5
        # dailyobject.day50 = set5
        # dailyobject.day57 = set5

        dailyobject.day6 = set6
        dailyobject.day13 = set6
        dailyobject.day20 = set6
        dailyobject.day27 = set6
        dailyobject.day34 = set6
        dailyobject.day41 = set6
        dailyobject.day48 = set6
        dailyobject.day55 = set6
        dailyobject.day62 = set6

        # dailyobject.day37 = set6
        # dailyobject.day44 = set6
        # dailyobject.day51 = set6
        # dailyobject.day58 = set6

        dailyobject.day7 = set7
        dailyobject.day14 = set7
        dailyobject.day21 = set7
        dailyobject.day28 = set7
        dailyobject.day35 = set7
        dailyobject.day42 = set7
        dailyobject.day49 = set7
        dailyobject.day56 = set7
        # dailyobject.day38 = set7
        # dailyobject.day45 = set7
        # dailyobject.day52 = set7
        # dailyobject.day59 = set7

        dailyobject.save()


        # return render(request, 'baker/join_baker.html', res_data)
    except DailyAmount.DoesNotExist:
        dailyobject = DailyAmount(
            businessID = businessID
        )

        if yoil == 0:  # 월요일
            if date % 7 == 0:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

            elif date % 7 == 1:
                set1, set2, set3, set4, set5, set6, set7 = monday, tuesday, wednesday, thursday, friday, saturday, sunday

            elif date % 7 == 2:
                set1, set2, set3, set4, set5, set6, set7 = sunday, monday, tuesday, wednesday, thursday, friday, saturday

            elif date % 7 == 3:
                set1, set2, set3, set4, set5, set6, set7 = saturday, sunday, monday, tuesday, wednesday, thursday, friday

            elif date % 7 == 4:
                set1, set2, set3, set4, set5, set6, set7 = friday, saturday, sunday, monday, tuesday, wednesday, thursday

            elif date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = thursday, friday, saturday, sunday, monday, tuesday, wednesday

            elif date % 7 == 6:
                set1, set2, set3, set4, set5, set6, set7 = wednesday, thursday, friday, saturday, sunday, monday, tuesday

        elif yoil == 1:  # 화요일
            if date % 7 == 1:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

            elif date % 7 == 2:
                set1, set2, set3, set4, set5, set6, set7 = monday, tuesday, wednesday, thursday, friday, saturday, sunday

            elif date % 7 == 3:
                set1, set2, set3, set4, set5, set6, set7 = sunday, monday, tuesday, wednesday, thursday, friday, saturday

            elif date % 7 == 4:
                set1, set2, set3, set4, set5, set6, set7 = saturday, sunday, monday, tuesday, wednesday, thursday, friday

            elif date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = friday, saturday, sunday, monday, tuesday, wednesday, thursday

            elif date % 7 == 6:
                set1, set2, set3, set4, set5, set6, set7 = thursday, friday, saturday, sunday, monday, tuesday, wednesday

            elif date % 7 == 0:
                set1, set2, set3, set4, set5, set6, set7 = wednesday, thursday, friday, saturday, sunday, monday, tuesday

        elif yoil == 2:  # 수요일
            if date % 7 == 2:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

            elif date % 7 == 3:
                set1, set2, set3, set4, set5, set6, set7 = monday, tuesday, wednesday, thursday, friday, saturday, sunday

            elif date % 7 == 4:
                set1, set2, set3, set4, set5, set6, set7 = sunday, monday, tuesday, wednesday, thursday, friday, saturday

            elif date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = saturday, sunday, monday, tuesday, wednesday, thursday, friday

            elif date % 7 == 6:
                set1, set2, set3, set4, set5, set6, set7 = friday, saturday, sunday, monday, tuesday, wednesday, thursday

            elif date % 7 == 0:
                set1, set2, set3, set4, set5, set6, set7 = thursday, friday, saturday, sunday, monday, tuesday, wednesday

            elif date % 7 == 1:
                set1, set2, set3, set4, set5, set6, set7 = wednesday, thursday, friday, saturday, sunday, monday, tuesday

        elif yoil == 3:  # 목요일
            if date % 7 == 3:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

            elif date % 7 == 4:
                set1, set2, set3, set4, set5, set6, set7 = monday, tuesday, wednesday, thursday, friday, saturday, sunday

            elif date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = sunday, monday, tuesday, wednesday, thursday, friday, saturday

            elif date % 7 == 6:
                set1, set2, set3, set4, set5, set6, set7 = saturday, sunday, monday, tuesday, wednesday, thursday, friday

            elif date % 7 == 0:
                set1, set2, set3, set4, set5, set6, set7 = friday, saturday, sunday, monday, tuesday, wednesday, thursday

            elif date % 7 == 1:
                set1, set2, set3, set4, set5, set6, set7 = thursday, friday, saturday, sunday, monday, tuesday, wednesday

            elif date % 7 == 2:
                set1, set2, set3, set4, set5, set6, set7 = wednesday, thursday, friday, saturday, sunday, monday, tuesday

        elif yoil == 4:  # 금요일
            if date % 7 == 4:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

            elif date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = sunday, monday, tuesday, wednesday, thursday, friday, saturday

            elif date % 7 == 6:
                set1, set2, set3, set4, set5, set6, set7 = sunday, monday, tuesday, wednesday, thursday, friday, saturday

            elif date % 7 == 0:
                set1, set2, set3, set4, set5, set6, set7 = saturday, sunday, monday, tuesday, wednesday, thursday, friday

            elif date % 7 == 1:
                set1, set2, set3, set4, set5, set6, set7 = friday, saturday, sunday, monday, tuesday, wednesday, thursday

            elif date % 7 == 2:
                set1, set2, set3, set4, set5, set6, set7 = thursday, friday, saturday, sunday, monday, tuesday, wednesday

            elif date % 7 == 3:
                set1, set2, set3, set4, set5, set6, set7 = wednesday, thursday, friday, saturday, sunday, monday, tuesday

        elif yoil == 5:  # 토요일
            if date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

            elif date % 7 == 6:
                set1, set2, set3, set4, set5, set6, set7 = monday, tuesday, wednesday, thursday, friday, saturday, sunday

            elif date % 7 == 0:
                set1, set2, set3, set4, set5, set6, set7 = sunday, monday, tuesday, wednesday, thursday, friday, saturday

            elif date % 7 == 1:
                set1, set2, set3, set4, set5, set6, set7 = saturday, sunday, monday, tuesday, wednesday, thursday, friday

            elif date % 7 == 2:
                set1, set2, set3, set4, set5, set6, set7 = friday, saturday, sunday, monday, tuesday, wednesday, thursday

            elif date % 7 == 3:
                set1, set2, set3, set4, set5, set6, set7 = thursday, friday, saturday, sunday, monday, tuesday, wednesday

            elif date % 7 == 4:
                set1, set2, set3, set4, set5, set6, set7 = wednesday, thursday, friday, saturday, sunday, monday, tuesday

        elif yoil == 6:  # 일요일
            if date % 7 == 6:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

            elif date % 7 == 0:
                set1, set2, set3, set4, set5, set6, set7 = monday, tuesday, wednesday, thursday, friday, saturday, sunday

            elif date % 7 == 1:
                set1, set2, set3, set4, set5, set6, set7 = sunday, monday, tuesday, wednesday, thursday, friday, saturday

            elif date % 7 == 2:
                set1, set2, set3, set4, set5, set6, set7 = saturday, sunday, monday, tuesday, wednesday, thursday, friday

            elif date % 7 == 3:
                set1, set2, set3, set4, set5, set6, set7 = friday, saturday, sunday, monday, tuesday, wednesday, thursday

            elif date % 7 == 4:
                set1, set2, set3, set4, set5, set6, set7 = thursday, friday, saturday, sunday, monday, tuesday, wednesday

            elif date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = wednesday, thursday, friday, saturday, sunday, monday, tuesday

        dailyobject.day1 = set1
        dailyobject.day8 = set1
        dailyobject.day15 = set1
        dailyobject.day22 = set1
        dailyobject.day29 = set1
        dailyobject.day36 = set1
        dailyobject.day43 = set1
        dailyobject.day50 = set1
        dailyobject.day57 = set1
        # dailyobject.day32 = set1
        # dailyobject.day39 = set1
        # dailyobject.day46 = set1
        # dailyobject.day53 = set1
        # dailyobject.day60 = set1

        dailyobject.day2 = set2
        dailyobject.day9 = set2
        dailyobject.day16 = set2
        dailyobject.day23 = set2
        dailyobject.day30 = set2
        dailyobject.day37 = set2
        dailyobject.day44 = set2
        dailyobject.day51 = set2
        dailyobject.day58 = set2
        # dailyobject.day33 = set2
        # dailyobject.day40 = set2
        # dailyobject.day47 = set2
        # dailyobject.day54 = set2
        # dailyobject.day61 = set2

        dailyobject.day3 = set3
        dailyobject.day10 = set3
        dailyobject.day17 = set3
        dailyobject.day24 = set3
        dailyobject.day31 = set3
        dailyobject.day38 = set3
        dailyobject.day45 = set3
        dailyobject.day52 = set3
        dailyobject.day59 = set3
        # dailyobject.day34 = set3
        # dailyobject.day41 = set3
        # dailyobject.day48 = set3
        # dailyobject.day55 = set3
        # dailyobject.day62 = set3

        dailyobject.day4 = set4
        dailyobject.day11 = set4
        dailyobject.day18 = set4
        dailyobject.day25 = set4
        dailyobject.day32 = set4
        dailyobject.day39 = set4
        dailyobject.day46 = set4
        dailyobject.day53 = set4
        dailyobject.day60 = set4

        # dailyobject.day35 = set4
        # dailyobject.day42 = set4
        # dailyobject.day49 = set4
        # dailyobject.day56 = set4

        dailyobject.day5 = set5
        dailyobject.day12 = set5
        dailyobject.day19 = set5
        dailyobject.day26 = set5
        dailyobject.day33 = set5
        dailyobject.day40 = set5
        dailyobject.day47 = set5
        dailyobject.day54 = set5
        dailyobject.day61 = set5

        # dailyobject.day36 = set5
        # dailyobject.day43 = set5
        # dailyobject.day50 = set5
        # dailyobject.day57 = set5

        dailyobject.day6 = set6
        dailyobject.day13 = set6
        dailyobject.day20 = set6
        dailyobject.day27 = set6
        dailyobject.day34 = set6
        dailyobject.day41 = set6
        dailyobject.day48 = set6
        dailyobject.day55 = set6
        dailyobject.day62 = set6

        # dailyobject.day37 = set6
        # dailyobject.day44 = set6
        # dailyobject.day51 = set6
        # dailyobject.day58 = set6

        dailyobject.day7 = set7
        dailyobject.day14 = set7
        dailyobject.day21 = set7
        dailyobject.day28 = set7
        dailyobject.day35 = set7
        dailyobject.day42 = set7
        dailyobject.day49 = set7
        dailyobject.day56 = set7
        # dailyobject.day38 = set7
        # dailyobject.day45 = set7
        # dailyobject.day52 = set7
        # dailyobject.day59 = set7

        dailyobject.save()