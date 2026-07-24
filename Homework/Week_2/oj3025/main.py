"""main"""
def main():
    """season"""
    month = int(input())
    day = int(input())
    season = ["winter", "spring", "summer", "fall"]
    ss = 0
    if month <= 3:
        ss = 0
    elif month <= 6:
        ss = 1
    elif month <= 9:
        ss = 2
    else:
        ss = 3
    if not month % 3 and day >=21:
        ss = (ss + 1) % 4
    print(season[ss])
main()
