from modify_day.date import get_date


def set_day_to_today():
    with open("./day/day.txt", "w") as f:
        euDay = get_date()
        f.write(euDay)
