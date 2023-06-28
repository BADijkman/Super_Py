from date import get_date


def reset_date_to_today():
    with open("./day/day.txt", "w") as f:
        euDay = get_date()
        f.write(euDay)
