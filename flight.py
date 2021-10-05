# Exercise 2.1 flight.py

def main():
    departures = {"dept1": 480, "dept2": 583, "dept3": 679, "dept4": 767,
                  "dept5": 840, "dept6": 945, "dept7": 1140, "dept8": 1305}
    arrivals = {"dept1": 616, "dept2": 712, "dept3": 811, "dept4": 900,
                "dept5": 968, "dept6": 1075, "dept7": 1280, "dept8": 1438}

    entertime = input("Please enter a time in a 24-hour time: ").split(":")
    entertime = (int(entertime[0]) * 60) + int(entertime[1])
    closest = find_closest(entertime, departures)

    print("The closest departure time is {}, arriving at {}".format(
        msm_to_24h(departures[closest]), msm_to_24h(arrivals[closest])))


def msm_to_24h(mins):
    AM = True
    hour = int(mins / 60)
    min = int(mins % 60)
    if hour >= 12:
        hour = hour - 12
        AM = 0
        if hour == 0:
            hour = 12
    return "{:02d}:{:02d} {}".format(int(hour), int(min), "a.m." if AM else "p.m.")


def find_closest(mins, departures):
    shortest = list(departures.keys())[0]
    shortest_diff = mins - departures[shortest]
    for d in departures:
        if(abs(mins-departures[d]) < shortest_diff):
            shortest = d
            shortest_diff = mins - departures[d]
    return shortest


if __name__ == "__main__":
    main()
