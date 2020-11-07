from .forms import *
from home.models import *
from datetime import datetime


def setDailyAmounts(businessID,sunday,monday,tuesday,wednesday,thursday,friday,saturday):

    date = datetime.today().day
    yoil = datetime.weekday(datetime.today())
    try:
        dailyobject = DailyAmount.objects.get(businessID=businessID)

        if yoil == 0:  # 일요일
            if date % 7 == 0:
                set1, set2, set3, set4, set5, set6, set7 = monday,tuesday,wednesday,thursday,friday,saturday,sunday

            elif date % 7 == 1:
                set1, set2, set3, set4, set5, set6, set7 = sunday, monday,tuesday,wednesday,thursday,friday,saturday

            elif date % 7 == 2:
                set1, set2, set3, set4, set5, set6, set7 = saturday,sunday, monday,tuesday,wednesday,thursday,friday

            elif date % 7 == 3:
                set1, set2, set3, set4, set5, set6, set7 = friday,saturday,sunday, monday,tuesday,wednesday,thursday

            elif date % 7 == 4:
                set1, set2, set3, set4, set5, set6, set7 = thursday,friday,saturday,sunday, monday,tuesday,wednesday

            elif date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = wednesday,thursday,friday,saturday,sunday, monday,tuesday

            elif date % 7 == 6:
                set1, set2, set3, set4, set5, set6, set7 = tuesday,wednesday,thursday,friday,saturday,sunday, monday

        elif yoil == 1:  # 월요일
            if date % 7 == 1:
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

            elif date % 7 == 0:
                set1, set2, set3, set4, set5, set6, set7 = tuesday,wednesday,thursday,friday,saturday,sunday, monday

        elif yoil == 2:  # 화요일
            if date % 7 == 2:
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

            elif date % 7 == 1:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

        elif yoil == 3:  # 화요일
            if date % 7 == 3:
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

            elif date % 7 == 2:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

        elif yoil == 4:  # 수요일
            if date % 7 == 4:
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

            elif date % 7 == 3:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

        elif yoil == 5:  # 목요일
            if date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = monday, tuesday, wednesday, thursday, friday, saturday, sunday

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

            elif date % 7 == 4:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

        elif yoil == 6:  # 금요일
            if date % 7 == 6:
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

            elif date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

        dailyobject.day1 = set1
        dailyobject.day8 = set1
        dailyobject.day15 = set1
        dailyobject.day22 = set1
        dailyobject.day29 = set1
        dailyobject.day32 = set1
        dailyobject.day39 = set1
        dailyobject.day46 = set1
        dailyobject.day53 = set1
        dailyobject.day60 = set1

        dailyobject.day2 = set2
        dailyobject.day9 = set2
        dailyobject.day16 = set2
        dailyobject.day23 = set2
        dailyobject.day30 = set2
        dailyobject.day33 = set2
        dailyobject.day40 = set2
        dailyobject.day47 = set2
        dailyobject.day54 = set2
        dailyobject.day61 = set2

        dailyobject.day3 = set3
        dailyobject.day10 = set3
        dailyobject.day17 = set3
        dailyobject.day24 = set3
        dailyobject.day31 = set3
        dailyobject.day34 = set3
        dailyobject.day41 = set3
        dailyobject.day48 = set3
        dailyobject.day55 = set3
        dailyobject.day62 = set3

        dailyobject.day4 = set4
        dailyobject.day11 = set4
        dailyobject.day18 = set4
        dailyobject.day25 = set4
        dailyobject.day35 = set4
        dailyobject.day42 = set4
        dailyobject.day49 = set4
        dailyobject.day56 = set4

        dailyobject.day5 = set5
        dailyobject.day12 = set5
        dailyobject.day19 = set5
        dailyobject.day26 = set5
        dailyobject.day36 = set5
        dailyobject.day43 = set5
        dailyobject.day50 = set5
        dailyobject.day57 = set5

        dailyobject.day6 = set6
        dailyobject.day13 = set6
        dailyobject.day20 = set6
        dailyobject.day27 = set6
        dailyobject.day37 = set6
        dailyobject.day44 = set6
        dailyobject.day51 = set6
        dailyobject.day58 = set6

        dailyobject.day7 = set7
        dailyobject.day14 = set7
        dailyobject.day21 = set7
        dailyobject.day28 = set7
        dailyobject.day38 = set7
        dailyobject.day45 = set7
        dailyobject.day52 = set7
        dailyobject.day59 = set7

        dailyobject.save()


        # return render(request, 'baker/join_baker.html', res_data)
    except DailyAmount.DoesNotExist:
        dailyobject = DailyAmount(
            businessID = businessID
        )

        if yoil == 0:  # 일요일
            if date % 7 == 0:
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

            elif date % 7 == 6:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

        elif yoil == 1:  # 월요일
            if date % 7 == 1:
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

            elif date % 7 == 0:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

        elif yoil == 2:  # 화요일
            if date % 7 == 2:
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

            elif date % 7 == 1:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

        elif yoil == 3:  # 화요일
            if date % 7 == 3:
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

            elif date % 7 == 2:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

        elif yoil == 4:  # 수요일
            if date % 7 == 4:
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

            elif date % 7 == 3:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

        elif yoil == 5:  # 목요일
            if date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = monday, tuesday, wednesday, thursday, friday, saturday, sunday

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

            elif date % 7 == 4:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

        elif yoil == 6:  # 금요일
            if date % 7 == 6:
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

            elif date % 7 == 5:
                set1, set2, set3, set4, set5, set6, set7 = tuesday, wednesday, thursday, friday, saturday, sunday, monday

        dailyobject.day1 = set1
        dailyobject.day8 = set1
        dailyobject.day15 = set1
        dailyobject.day22 = set1
        dailyobject.day29 = set1
        dailyobject.day32 = set1
        dailyobject.day39 = set1
        dailyobject.day46 = set1
        dailyobject.day53 = set1
        dailyobject.day60 = set1

        dailyobject.day2 = set2
        dailyobject.day9 = set2
        dailyobject.day16 = set2
        dailyobject.day23 = set2
        dailyobject.day30 = set2
        dailyobject.day33 = set2
        dailyobject.day40 = set2
        dailyobject.day47 = set2
        dailyobject.day54 = set2
        dailyobject.day61 = set2

        dailyobject.day3 = set3
        dailyobject.day10 = set3
        dailyobject.day17 = set3
        dailyobject.day24 = set3
        dailyobject.day31 = set3
        dailyobject.day34 = set3
        dailyobject.day41 = set3
        dailyobject.day48 = set3
        dailyobject.day55 = set3
        dailyobject.day62 = set3

        dailyobject.day4 = set4
        dailyobject.day11 = set4
        dailyobject.day18 = set4
        dailyobject.day25 = set4
        dailyobject.day35 = set4
        dailyobject.day42 = set4
        dailyobject.day49 = set4
        dailyobject.day56 = set4

        dailyobject.day5 = set5
        dailyobject.day12 = set5
        dailyobject.day19 = set5
        dailyobject.day26 = set5
        dailyobject.day36 = set5
        dailyobject.day43 = set5
        dailyobject.day50 = set5
        dailyobject.day57 = set5

        dailyobject.day6 = set6
        dailyobject.day13 = set6
        dailyobject.day20 = set6
        dailyobject.day27 = set6
        dailyobject.day37 = set6
        dailyobject.day44 = set6
        dailyobject.day51 = set6
        dailyobject.day58 = set6

        dailyobject.day7 = set7
        dailyobject.day14 = set7
        dailyobject.day21 = set7
        dailyobject.day28 = set7
        dailyobject.day38 = set7
        dailyobject.day45 = set7
        dailyobject.day52 = set7
        dailyobject.day59 = set7

        dailyobject.save()

        # dailyobject.day7 = sunday
        # dailyobject.day14 = sunday
        # dailyobject.day21 = sunday
        # dailyobject.day28 = sunday
        # dailyobject.day38 = sunday
        # dailyobject.day45 = sunday
        # dailyobject.day52 = sunday
        # dailyobject.day59 = sunday
        #
        # dailyobject.day1 = monday
        # dailyobject.day8 = monday
        # dailyobject.day15 = monday
        # dailyobject.day22 = monday
        # dailyobject.day29 = monday
        # dailyobject.day32 = monday
        # dailyobject.day39 = monday
        # dailyobject.day46 = monday
        # dailyobject.day53 = monday
        # dailyobject.day60 = monday
        #
        # dailyobject.day2 = tuesday
        # dailyobject.day9 = tuesday
        # dailyobject.day16 = tuesday
        # dailyobject.day23 = tuesday
        # dailyobject.day30 = tuesday
        # dailyobject.day33 = tuesday
        # dailyobject.day40 = tuesday
        # dailyobject.day47 = tuesday
        # dailyobject.day54 = tuesday
        # dailyobject.day61 = tuesday
        #
        # dailyobject.day3 = wednesday
        # dailyobject.day10 = wednesday
        # dailyobject.day17 = wednesday
        # dailyobject.day24 = wednesday
        # dailyobject.day31 = wednesday
        # dailyobject.day34 = wednesday
        # dailyobject.day41 = wednesday
        # dailyobject.day48 = wednesday
        # dailyobject.day55 = wednesday
        # dailyobject.day62 = wednesday
        #
        # dailyobject.day4 = thursday
        # dailyobject.day11 = thursday
        # dailyobject.day18 = thursday
        # dailyobject.day25 = thursday
        # dailyobject.day35 = thursday
        # dailyobject.day42 = thursday
        # dailyobject.day49 = thursday
        # dailyobject.day56 = thursday
        #
        # dailyobject.day5 = friday
        # dailyobject.day12 = friday
        # dailyobject.day19 = friday
        # dailyobject.day26 = friday
        # dailyobject.day36 = friday
        # dailyobject.day43 = friday
        # dailyobject.day50 = friday
        # dailyobject.day57 = friday
        #
        # dailyobject.day6 = saturday
        # dailyobject.day13 = saturday
        # dailyobject.day20 = saturday
        # dailyobject.day27 = saturday
        # dailyobject.day37 = saturday
        # dailyobject.day44 = saturday
        # dailyobject.day51 = saturday
        # dailyobject.day58 = saturday
        #
        # dailyobject.day1 = sunday
        # dailyobject.day8 = sunday
        # dailyobject.day15 = sunday
        # dailyobject.day22 = sunday
        # dailyobject.day29 = sunday
        # dailyobject.day32 = sunday
        # dailyobject.day39 = sunday
        # dailyobject.day46 = sunday
        # dailyobject.day53 = sunday
        # dailyobject.day60 = sunday
        #
        # dailyobject.day2 = monday
        # dailyobject.day9 = monday
        # dailyobject.day16 = monday
        # dailyobject.day23 = monday
        # dailyobject.day30 = monday
        # dailyobject.day33 = monday
        # dailyobject.day40 = monday
        # dailyobject.day47 = monday
        # dailyobject.day54 = monday
        # dailyobject.day61 = monday
        #
        # dailyobject.day3 = tuesday
        # dailyobject.day10 = tuesday
        # dailyobject.day17 = tuesday
        # dailyobject.day24 = tuesday
        # dailyobject.day31 = tuesday
        # dailyobject.day34 = tuesday
        # dailyobject.day41 = tuesday
        # dailyobject.day48 = tuesday
        # dailyobject.day55 = tuesday
        # dailyobject.day62 = tuesday
        #
        # dailyobject.day4 = wednesday
        # dailyobject.day11 = wednesday
        # dailyobject.day18 = wednesday
        # dailyobject.day25 = wednesday
        # dailyobject.day35 = wednesday
        # dailyobject.day42 = wednesday
        # dailyobject.day49 = wednesday
        # dailyobject.day56 = wednesday
        #
        # dailyobject.day5 = thursday
        # dailyobject.day12 = thursday
        # dailyobject.day19 = thursday
        # dailyobject.day26 = thursday
        # dailyobject.day36 = thursday
        # dailyobject.day43 = thursday
        # dailyobject.day50 = thursday
        # dailyobject.day57 = thursday
        #
        # dailyobject.day6 = friday
        # dailyobject.day13 = friday
        # dailyobject.day20 = friday
        # dailyobject.day27 = friday
        # dailyobject.day37 = friday
        # dailyobject.day44 = friday
        # dailyobject.day51 = friday
        # dailyobject.day58 = friday
        #
        # dailyobject.day7 = saturday
        # dailyobject.day14 = saturday
        # dailyobject.day21 = saturday
        # dailyobject.day28 = saturday
        # dailyobject.day38 = saturday
        # dailyobject.day45 = saturday
        # dailyobject.day52 = saturday
        # dailyobject.day59 = saturday
        #
        # dailyobject.day2 = sunday
        # dailyobject.day9 = sunday
        # dailyobject.day16 = sunday
        # dailyobject.day23 = sunday
        # dailyobject.day30 = sunday
        # dailyobject.day33 = sunday
        # dailyobject.day40 = sunday
        # dailyobject.day47 = sunday
        # dailyobject.day54 = sunday
        # dailyobject.day61 = sunday
        #
        # dailyobject.day3 = monday
        # dailyobject.day10 = monday
        # dailyobject.day17 = monday
        # dailyobject.day24 = monday
        # dailyobject.day31 = monday
        # dailyobject.day34 = monday
        # dailyobject.day41 = monday
        # dailyobject.day48 = monday
        # dailyobject.day55 = monday
        # dailyobject.day62 = monday
        #
        # dailyobject.day4 = tuesday
        # dailyobject.day11 = tuesday
        # dailyobject.day18 = tuesday
        # dailyobject.day25 = tuesday
        # dailyobject.day35 = tuesday
        # dailyobject.day42 = tuesday
        # dailyobject.day49 = tuesday
        # dailyobject.day56 = tuesday
        #
        # dailyobject.day5 = wednesday
        # dailyobject.day12 = wednesday
        # dailyobject.day19 = wednesday
        # dailyobject.day26 = wednesday
        # dailyobject.day36 = wednesday
        # dailyobject.day43 = wednesday
        # dailyobject.day50 = wednesday
        # dailyobject.day57 = wednesday
        #
        # dailyobject.day6 = thursday
        # dailyobject.day13 = thursday
        # dailyobject.day20 = thursday
        # dailyobject.day27 = thursday
        # dailyobject.day37 = thursday
        # dailyobject.day44 = thursday
        # dailyobject.day51 = thursday
        # dailyobject.day58 = thursday
        #
        # dailyobject.day7 = friday
        # dailyobject.day14 = friday
        # dailyobject.day21 = friday
        # dailyobject.day28 = friday
        # dailyobject.day38 = friday
        # dailyobject.day45 = friday
        # dailyobject.day52 = friday
        # dailyobject.day59 = friday
        #
        # dailyobject.day1 = saturday
        # dailyobject.day8 = saturday
        # dailyobject.day15 = saturday
        # dailyobject.day22 = saturday
        # dailyobject.day29 = saturday
        # dailyobject.day32 = saturday
        # dailyobject.day39 = saturday
        # dailyobject.day46 = saturday
        # dailyobject.day53 = saturday
        # dailyobject.day60 = saturday
        #
        # dailyobject.day3 = sunday
        # dailyobject.day10 = sunday
        # dailyobject.day17 = sunday
        # dailyobject.day24 = sunday
        # dailyobject.day31 = sunday
        # dailyobject.day34 = sunday
        # dailyobject.day41 = sunday
        # dailyobject.day48 = sunday
        # dailyobject.day55 = sunday
        # dailyobject.day62 = sunday
        #
        # dailyobject.day4 = monday
        # dailyobject.day11 = monday
        # dailyobject.day18 = monday
        # dailyobject.day25 = monday
        # dailyobject.day35 = monday
        # dailyobject.day42 = monday
        # dailyobject.day49 = monday
        # dailyobject.day56 = monday
        #
        # dailyobject.day5 = tuesday
        # dailyobject.day12 = tuesday
        # dailyobject.day19 = tuesday
        # dailyobject.day26 = tuesday
        # dailyobject.day36 = tuesday
        # dailyobject.day43 = tuesday
        # dailyobject.day50 = tuesday
        # dailyobject.day57 = tuesday
        #
        # dailyobject.day6 = wednesday
        # dailyobject.day13 = wednesday
        # dailyobject.day20 = wednesday
        # dailyobject.day27 = wednesday
        # dailyobject.day37 = wednesday
        # dailyobject.day44 = wednesday
        # dailyobject.day51 = wednesday
        # dailyobject.day58 = wednesday
        #
        # dailyobject.day7 = thursday
        # dailyobject.day14 = thursday
        # dailyobject.day21 = thursday
        # dailyobject.day28 = thursday
        # dailyobject.day38 = thursday
        # dailyobject.day45 = thursday
        # dailyobject.day52 = thursday
        # dailyobject.day59 = thursday
        #
        # dailyobject.day1 = friday
        # dailyobject.day8 = friday
        # dailyobject.day15 = friday
        # dailyobject.day22 = friday
        # dailyobject.day29 = friday
        # dailyobject.day32 = friday
        # dailyobject.day39 = friday
        # dailyobject.day46 = friday
        # dailyobject.day53 = friday
        # dailyobject.day60 = friday
        #
        # dailyobject.day2 = saturday
        # dailyobject.day9 = saturday
        # dailyobject.day16 = saturday
        # dailyobject.day23 = saturday
        # dailyobject.day30 = saturday
        # dailyobject.day33 = saturday
        # dailyobject.day40 = saturday
        # dailyobject.day47 = saturday
        # dailyobject.day54 = saturday
        # dailyobject.day61 = saturday
        #
        # dailyobject.day4 = sunday
        # dailyobject.day11 = sunday
        # dailyobject.day18 = sunday
        # dailyobject.day25 = sunday
        # dailyobject.day35 = sunday
        # dailyobject.day42 = sunday
        # dailyobject.day49 = sunday
        # dailyobject.day56 = sunday
        #
        # dailyobject.day5 = monday
        # dailyobject.day12 = monday
        # dailyobject.day19 = monday
        # dailyobject.day26 = monday
        # dailyobject.day36 = monday
        # dailyobject.day43 = monday
        # dailyobject.day50 = monday
        # dailyobject.day57 = monday
        #
        # dailyobject.day6 = tuesday
        # dailyobject.day13 = tuesday
        # dailyobject.day20 = tuesday
        # dailyobject.day27 = tuesday
        # dailyobject.day37 = tuesday
        # dailyobject.day44 = tuesday
        # dailyobject.day51 = tuesday
        # dailyobject.day58 = tuesday
        #
        # dailyobject.day7 = wednesday
        # dailyobject.day14 = wednesday
        # dailyobject.day21 = wednesday
        # dailyobject.day28 = wednesday
        # dailyobject.day38 = wednesday
        # dailyobject.day45 = wednesday
        # dailyobject.day52 = wednesday
        # dailyobject.day59 = wednesday
        #
        # dailyobject.day1 = thursday
        # dailyobject.day8 = thursday
        # dailyobject.day15 = thursday
        # dailyobject.day22 = thursday
        # dailyobject.day29 = thursday
        # dailyobject.day32 = thursday
        # dailyobject.day39 = thursday
        # dailyobject.day46 = thursday
        # dailyobject.day53 = thursday
        # dailyobject.day60 = thursday
        #
        # dailyobject.day2 = friday
        # dailyobject.day9 = friday
        # dailyobject.day16 = friday
        # dailyobject.day23 = friday
        # dailyobject.day30 = friday
        # dailyobject.day33 = friday
        # dailyobject.day40 = friday
        # dailyobject.day47 = friday
        # dailyobject.day54 = friday
        # dailyobject.day61 = friday
        #
        # dailyobject.day3 = saturday
        # dailyobject.day10 = saturday
        # dailyobject.day17 = saturday
        # dailyobject.day24 = saturday
        # dailyobject.day31 = saturday
        # dailyobject.day34 = saturday
        # dailyobject.day41 = saturday
        # dailyobject.day48 = saturday
        # dailyobject.day55 = saturday
        # dailyobject.day62 = saturday
        #
        # dailyobject.day5 = sunday
        # dailyobject.day12 = sunday
        # dailyobject.day19 = sunday
        # dailyobject.day26 = sunday
        # dailyobject.day36 = sunday
        # dailyobject.day43 = sunday
        # dailyobject.day50 = sunday
        # dailyobject.day57 = sunday
        #
        # dailyobject.day6 = monday
        # dailyobject.day13 = monday
        # dailyobject.day20 = monday
        # dailyobject.day27 = monday
        # dailyobject.day37 = monday
        # dailyobject.day44 = monday
        # dailyobject.day51 = monday
        # dailyobject.day58 = monday
        #
        # dailyobject.day7 = tuesday
        # dailyobject.day14 = tuesday
        # dailyobject.day21 = tuesday
        # dailyobject.day28 = tuesday
        # dailyobject.day38 = tuesday
        # dailyobject.day45 = tuesday
        # dailyobject.day52 = tuesday
        # dailyobject.day59 = tuesday
        #
        # dailyobject.day1 = wednesday
        # dailyobject.day8 = wednesday
        # dailyobject.day15 = wednesday
        # dailyobject.day22 = wednesday
        # dailyobject.day29 = wednesday
        # dailyobject.day32 = wednesday
        # dailyobject.day39 = wednesday
        # dailyobject.day46 = wednesday
        # dailyobject.day53 = wednesday
        # dailyobject.day60 = wednesday
        #
        # dailyobject.day2 = thursday
        # dailyobject.day9 = thursday
        # dailyobject.day16 = thursday
        # dailyobject.day23 = thursday
        # dailyobject.day30 = thursday
        # dailyobject.day33 = thursday
        # dailyobject.day40 = thursday
        # dailyobject.day47 = thursday
        # dailyobject.day54 = thursday
        # dailyobject.day61 = thursday
        #
        # dailyobject.day3 = friday
        # dailyobject.day10 = friday
        # dailyobject.day17 = friday
        # dailyobject.day24 = friday
        # dailyobject.day31 = friday
        # dailyobject.day34 = friday
        # dailyobject.day41 = friday
        # dailyobject.day48 = friday
        # dailyobject.day55 = friday
        # dailyobject.day62 = friday
        #
        # dailyobject.day4 = saturday
        # dailyobject.day11 = saturday
        # dailyobject.day18 = saturday
        # dailyobject.day25 = saturday
        # dailyobject.day35 = saturday
        # dailyobject.day42 = saturday
        # dailyobject.day49 = saturday
        # dailyobject.day56 = saturday