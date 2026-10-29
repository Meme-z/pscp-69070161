"""ig"""
def dig(op, d):
    """wow"""
    n = []
    for i in range(10):
        if op == "==" and i == d:
            n.append(i)
        elif op == "!=" and i != d:
            n.append(i)
        elif op == ">" and i > d:
            n.append(i)
        elif op == "<" and i < d:
            n.append(i)
        elif op == ">=" and i >= d:
            n.append(i)
        elif op == "<=" and i <= d:
            n.append(i)
    return n

num = input().split()
num2 = input().split()
num3 = input().split()
dnum = dig(num[0],int(num[1]))
tnum = dig(num2[0],int(num2[1]))
hnum = dig(num3[0],int(num3[1]))
for h in hnum:
    for s in tnum:
        for f in dnum:
            print(f"{h}{s}{f}")
