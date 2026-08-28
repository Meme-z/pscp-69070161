"""wow"""
def main():
    """wow"""
    info = input().split()
    age = int(info[0])
    day = info[1]
    pay = 0
    if age < 5:
        pay = 0
    elif age <= 18:
        pay = 100
    elif age >= 19:
        pay = 150
    if day == "Wed":
        pay /= 2
    print(int(pay))
main()
