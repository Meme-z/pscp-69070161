"""main"""
def main():
    """temp"""
    temp = float(input())
    unit = input().lower()
    cunit = input().lower()
    cels = 0
    if unit == "c" :
        cels = temp
    elif unit == "k":
        cels = temp - 273.15
    elif unit == "f":
        cels = (temp - 32) * 5 / 9
    elif unit == "r":
        cels = (temp - 491.67) * 5 / 9
    if cunit == "c":
        temp = cels
    elif cunit == "k":
        temp = cels + 273.15
    elif cunit == "f":
        temp = cels * 9 / 5 + 32
    elif cunit == "r":
        temp = (cels + 273.15) * 9 / 5
    print(f"{temp:.2f}")
main()
