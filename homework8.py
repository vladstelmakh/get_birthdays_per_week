from datetime import datetime, timedelta

test_list = [
    {"name": "Bill", "birthday": datetime(1990, 4, 5)},
    {"name": "Kim", "birthday": datetime(1985, 4, 5)},
    {"name": "Jill", "birthday": datetime(1982, 4, 5)},
    {"name": "Jan", "birthday": datetime(1995, 4, 6)},
    {"name": "Eve", "birthday": datetime(1992, 4, 9)},
    {"name": "Emily", "birthday": datetime(1990, 4, 6)},
    {"name": "Antony", "birthday": datetime(1985, 4, 12)},
    {"name": "Jill", "birthday": datetime(1982, 4, 7)},
    {"name": "Jan", "birthday": datetime(1995, 4, 8)}
]


def get_birthdays_per_week(bday_list):
    bday_dict = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }

    today = datetime.today().date()
    start_date = today + timedelta(days=1)
    end_date = start_date + timedelta(days=6)

    for person in bday_list:
        bday_month = person["birthday"].month
        bday_day = person["birthday"].day
        bday = datetime(today.year, bday_month, bday_day).date()
        if start_date <= bday <= end_date:
            bday_day = bday.strftime("%A")
            if bday_day == "Saturday" or bday_day == "Sunday":
                bday_day = "Monday"
            bday_dict[bday_day].append(person["name"])

    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
        if bday_dict[day]:
            print(f"{day}: {', '.join(bday_dict[day])}")


get_birthdays_per_week(test_list)
