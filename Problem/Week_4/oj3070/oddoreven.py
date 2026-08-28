"""oddeven"""
def main():
    """wow"""
    od = 0
    ev = 0
    for _ in range(3):
        num = int(input())
        if num %2 ==1:
            od+=1
        else:
            ev+=1
    print(ev)
    print(od)
main()
