from datetime import date, timedelta


def sundays():
    dt = date(1901, 1, 7)
    assert not dt.weekday()
    week = timedelta(7)
    count = 0
    while dt.year < 2000:
        dt += week
        count += (dt.day == 1)
    return count


if __name__ == '__main__':
    print(sundays())
