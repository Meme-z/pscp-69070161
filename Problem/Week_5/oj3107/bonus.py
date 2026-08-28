"""wow"""
def main():
    """wow"""
    info = input().split()
    bonus = 0
    rank = info[0]
    year = int(info[1])
    money = int(info[2])
    if rank == "M":
        if year <= 5:
            bonus = money*0.06+1500
        elif year <= 10:
            bonus = money*0.08+1500
        elif year > 10:
            bonus = money*0.1+1500
    if rank == "B":
        if year <= 5:
            bonus = money*0.05+1000
        elif year <= 10:
            bonus = money*0.06+1000
        elif year > 10:
            bonus = money*0.07+1000
    if rank == "G":
        if year <= 5:
            bonus = money*0.04+500
        elif year <= 10:
            bonus = money*0.05+500
        elif year > 10:
            bonus = money*0.06+500
    print(int(bonus))
main()
