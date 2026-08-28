"""wow"""
from math import ceil
def main():
    """wow"""
    stime = input().split(".")
    etime = input().split(".")
    pay = 0
    if int(stime[0]) > 23 or int(stime[1]) >59 or int(etime[0]) > 23 or int(etime[1]) >59:
        print("ERROR")
    else:
        dtime = int(etime[0])*60+int(etime[1])-int(stime[0])*60-int(stime[1])
        if dtime < 0:
            print("ERROR")
        elif dtime <= 15:
            print("FREE")
        elif dtime > 15:
            dtime = ceil(dtime/60)
            if dtime <= 2:
                pay = dtime * 25
            elif dtime <= 4:
                pay = 50+(dtime-2)*30
            elif dtime <= 6:
                pay = 110+(dtime-4)*35
            elif dtime >= 7:
                pay = 250
            print(pay)
main()
